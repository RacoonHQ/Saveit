# Saveit

A flexible and silent media saver for Telegram, running in **Userbot Mode** (saves self-destructing/timed photos & videos from chats to your Saved Messages).

---

## Features

* **Self-Destructing Media Support**: Automatically saves timed/self-destructing media from any chat.
* **Multi-Account Support**: Run multiple accounts simultaneously by configuring `API_ID_1`, `API_ID_2`, etc.
* **Zero Compression**: Forwards downloaded media back to your **Saved Messages** as original document files, preserving full quality.
* **EXIF Metadata Reader**: Extracts and appends metadata (Device Model, Taken Time) for photos if available.
* **Flexible Handler**: 
  * Reply to any media with your custom handler (e.g. `.saveit`).
  * If the handler is left empty, **automatic saving** is enabled (simply reply to any media to save it).
* **Silent & Background Operation**: Runs completely in the background without sending chat notifications.

---

## Requirements

* **Python 3.9+**
* Dependencies: `telethon`, `python-dotenv`, `pillow`.

### Install all dependencies manually:
```bash
pip install -r requirements.txt
```
*(Or let the helper scripts install them automatically)*

---

## Configuration (`.env`)

Create a `.env` file in the root directory (or copy `.env.example`).

```ini
API_ID_1=123456
API_HASH_1=abcdef1234567890abcdef1234567890

# (Optional) Multiple account configurations
# API_ID_2=789012
# API_HASH_2=fedcba0987654321fedcba0987654321

# Trigger command. Leave empty for automatic saving on any reply.
HANDLER=.saveit
```

---

## Quick Start

### Windows (Automatic Script)
Simply run `run.bat`. It will create `.env`, ask for your API credentials, install required dependencies, and launch Userbot Mode:
```cmd
run.bat
```

### Linux / macOS (Automatic Script)
```bash
chmod +x run.sh
./run.sh
```

---

## How to Use

Start the userbot:
```bash
python Saveit.py
```
* **Command Mode (HANDLER is set, e.g., `.saveit`)**: Reply to any media message in any Telegram chat with `.saveit`.
* **Auto Mode (HANDLER is empty)**: Simply reply to any media message in any Telegram chat.
* **Result**: The media is saved to the local `downloads/` directory and forwarded to your **Saved Messages** with sender info & image EXIF metadata (if any).

---

## Support & Contributions

For any issues or suggestions, feel free to open a ticket or reach out:
* **GitHub Issues**: [Issues Page](https://github.com/RacoonHQ/Saveit/issues)
