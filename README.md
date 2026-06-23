# Saveit

A flexible and silent media saver for Telegram, supporting both **Userbot Mode** (saves self-destructing/timed photos & videos from chats to your Saved Messages) and **Bot Mode** (runs as a dedicated bot that accepts and saves forwarded/direct media).

---

## Features

### Userbot Mode (`Saveit.py`)
* **Self-Destructing Media Support**: Automatically saves timed/self-destructing media from any chat.
* **Multi-Account Support**: Run multiple accounts simultaneously by configuring `API_ID_1`, `API_ID_2`, etc.
* **Zero Compression**: Forwards downloaded media back to your **Saved Messages** as original document files, preserving full quality.
* **EXIF Metadata Reader**: Extracts and appends metadata (Device Model, Taken Time, GPS Location with Google Maps link) for photos if available.
* **Flexible Handler**: 
  * Reply to any media with your custom handler (e.g. `.saveit`).
  * If the handler is left empty, **automatic saving** is enabled (simply reply to any media to save it).
* **Silent & Background Operation**: Runs completely in the background without sending chat notifications.

### Bot Mode (`Saveit_bot.py`)
* **Dedicated Bot**: Run a standalone Telegram bot using a Token from `@BotFather`.
* **Access Control / Whitelist**: Control who can use the bot using `ALLOWED_USERS` in `.env` and runtime auto-registration (stored in `registered_users.json`).
* **Auto-Save Mode**: Automatically downloads and sends back any media sent directly to the bot.
* **Manual Handler Mode**: Reply to any media in the bot chat with your handler (e.g., `.save`) to save it.

---

## Requirements

* **Python 3.9+**
* Dependencies: `telethon`, `python-telegram-bot` (only for Bot Mode), `python-dotenv`, `pillow`.

### Install all dependencies manually:
```bash
pip install -r requirements.txt
```
*(Or let the helper scripts install them automatically)*

---

## Configuration (`.env`)

Create a `.env` file in the root directory (or copy `.env.example`).

```ini
# ==========================================
# USERBOT MODE (Saveit.py)
# ==========================================
API_ID_1=123456
API_HASH_1=abcdef1234567890abcdef1234567890

# (Optional) Multiple account configurations
# API_ID_2=789012
# API_HASH_2=fedcba0987654321fedcba0987654321

# Trigger command. Leave empty for automatic saving on any reply.
HANDLER=.saveit

# ==========================================
# BOT MODE (Saveit_bot.py)
# ==========================================
BOT_TOKEN=your_bot_token_here
ALLOWED_USERS=123456789,987654321
AUTO_SAVE=true
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

### 1. Userbot Mode (`Saveit.py`)
Start the userbot:
```bash
python Saveit.py
```
* **Command Mode (HANDLER is set, e.g., `.saveit`)**: Reply to any media message in any Telegram chat with `.saveit`.
* **Auto Mode (HANDLER is empty)**: Simply reply to any media message in any Telegram chat.
* **Result**: The media is saved to the local `downloads/` directory and forwarded to your **Saved Messages** with sender info & image EXIF metadata (if any).

### 2. Bot Mode (`Saveit_bot.py`)
Start the bot:
```bash
python Saveit_bot.py
```
* **Direct Mode**: Send any media directly to the bot.
* **Reply Mode**: Reply to any media in the chat with your handler (e.g. `.save`).

---

## Support & Contributions

For any issues or suggestions, feel free to open a ticket or reach out:
* **GitHub Issues**: [Issues Page](https://github.com/RacoonHQ/Saveit/issues)
