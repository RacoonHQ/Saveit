from telethon import TelegramClient, events
import os
import re
from dotenv import load_dotenv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_metadata(file_path):
    metadata = {}
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if not exif_data:
                return metadata
            
            raw_exif = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                raw_exif[tag] = value
            
            # 1. Device Info (Make & Model)
            make = raw_exif.get("Make", "")
            model = raw_exif.get("Model", "")
            if make or model:
                if make and model:
                    make_str = str(make).replace('\x00', '').strip()
                    model_str = str(model).replace('\x00', '').strip()
                    if model_str.lower().startswith(make_str.lower()):
                        metadata["device"] = model_str
                    else:
                        metadata["device"] = f"{make_str} {model_str}"
                else:
                    metadata["device"] = str(make or model).replace('\x00', '').strip()
            
            # 2. Taken Time
            date_time = raw_exif.get("DateTimeOriginal") or raw_exif.get("DateTime")
            if date_time:
                metadata["taken_at"] = str(date_time).strip()
            
            # 3. GPS Location
            gps_info = raw_exif.get("GPSInfo")
            if gps_info:
                gps_data = {}
                for t in gps_info:
                    sub_tag = GPSTAGS.get(t, t)
                    gps_data[sub_tag] = gps_info[t]
                
                def get_decimal_from_dms(dms, ref):
                    def to_float(val):
                        try:
                            return float(val)
                        except (TypeError, ValueError):
                            if hasattr(val, 'numerator') and hasattr(val, 'denominator'):
                                return float(val.numerator) / float(val.denominator)
                            return 0.0
                    
                    if len(dms) >= 3:
                        d = to_float(dms[0])
                        m = to_float(dms[1])
                        s = to_float(dms[2])
                        decimal = d + (m / 60.0) + (s / 3600.0)
                        if ref in ['S', 'W']:
                            decimal = -decimal
                        return decimal
                    return 0.0
                
                lat_dms = gps_data.get("GPSLatitude")
                lat_ref = gps_data.get("GPSLatitudeRef")
                lon_dms = gps_data.get("GPSLongitude")
                lon_ref = gps_data.get("GPSLongitudeRef")
                
                if lat_dms and lat_ref and lon_dms and lon_ref:
                    lat = get_decimal_from_dms(lat_dms, lat_ref)
                    lon = get_decimal_from_dms(lon_dms, lon_ref)
                    metadata["location"] = f"{lat:.6f}, {lon:.6f}"
                    metadata["google_maps_url"] = f"https://www.google.com/maps?q={lat},{lon}"
    except Exception:
        pass
    return metadata


# Load environment variables
load_dotenv()

handler = os.getenv('HANDLER', '').strip()

# Collect all accounts from .env
accounts = []
i = 1
while True:
    api_id = os.getenv(f'API_ID_{i}')
    api_hash = os.getenv(f'API_HASH_{i}')
    if not api_id or not api_hash:
        break
    try:
        api_id = int(api_id)
    except ValueError:
        print(f"❌ Account {i}: API_ID must be an integer")
        i += 1
        continue
    accounts.append((i, api_id, api_hash))
    i += 1

if not accounts:
    raise RuntimeError("No valid accounts found in .env (use API_ID_1, API_HASH_1, etc.)")

# Initialize clients
clients = []
for acc_num, api_id, api_hash in accounts:
    client = TelegramClient(f'saveit_session_{acc_num}', api_id, api_hash)
    clients.append((acc_num, client, None))

# Download path
download_path = "downloads"
if not os.path.exists(download_path):
    os.makedirs(download_path)

def create_handler(client, your_user_id_holder):
    @client.on(events.NewMessage())
    async def download(event):
        # Get user ID once
        if your_user_id_holder[0] is None:
            me = await client.get_me()
            your_user_id_holder[0] = me.id

        # Only owner can use
        if event.sender_id != your_user_id_holder[0]:
            return  # Silent: no reply

        # If handler is configured, match the pattern
        if handler:
            if not event.text or not re.match(rf'^{re.escape(handler)}(\s+|$)', event.text):
                return

        # Must be a reply
        if not event.is_reply:
            return  # Silent: no message

        reply_msg = await event.get_reply_message()

        # Must have media
        if not reply_msg or not reply_msg.media:
            return  # Silent: no notification

        # Download silently
        try:
            file_path = await client.download_media(
                reply_msg,
                file=os.path.join(download_path, "")
            )
            if not file_path:
                print("DEBUG: download_media returned None or empty path")
                return  # Failed to download, silent
            print(f"DEBUG: Downloaded media path: {file_path}")
        except Exception as e:
            print(f"DEBUG: download_media failed: {e}")
            return  # Ignore error, silent

        # Send to Saved Messages silently
        try:
            sender = reply_msg.sender
            username = f"@{sender.username}" if sender and sender.username else f"User {reply_msg.sender_id}"
            phone = getattr(sender, 'phone', None)
            phone_str = f" (+{phone})" if phone else ""
            caption = f"📎 Saved from: {username}{phone_str}\n📅 {reply_msg.date.strftime('%Y-%m-%d %H:%M')}"

            # Check if file has metadata
            ext = os.path.splitext(file_path)[1].lower()
            print(f"DEBUG: File extension: {ext}")
            if ext in ['.jpg', '.jpeg', '.png', '.webp', '.tiff', '.mpo']:
                meta = get_image_metadata(file_path)
                print(f"DEBUG: Extracted metadata: {meta}")
                if meta:
                    caption += "\n\nℹ️ **Image Metadata:**"
                    if "device" in meta:
                        caption += f"\n📱 Device: {meta['device']}"
                    if "taken_at" in meta:
                        caption += f"\n📅 Taken at: {meta['taken_at']}"
                    if "location" in meta:
                        caption += f"\n📍 Location: [{meta['location']}]({meta['google_maps_url']})"
                else:
                    print("DEBUG: get_image_metadata returned empty or None")

            await client.send_file(
                'me',
                file_path,
                caption=caption,
                force_document=True,
                silent=True  # No notification
            )

            # Clean up
            os.remove(file_path)
        except Exception:
            pass  # Ignore send error, silent
    return download

# Register handlers for each client
for acc_num, client, _ in clients:
    create_handler(client, [None])

# Main
async def main():
    async with clients[0][1]:
        # Start all other clients
        for acc_num, client, _ in clients[1:]:
            await client.start()
        
        # Print status for all accounts
        for acc_num, client, _ in clients:
            me = await client.get_me()
            print(f"✅ Account {acc_num} running as @{me.username}")
        if handler:
            print(f"🤫 Use '{handler}' to save media (no alerts shown)")
        else:
            print("🤫 Automatic saving enabled (no handler: reply to any media to save it)")
        
        # Run until disconnected (first client keeps the loop alive)
        await clients[0][1].run_until_disconnected()
        
        # Disconnect all other clients
        for acc_num, client, _ in clients[1:]:
            await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())