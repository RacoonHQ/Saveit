#!/bin/bash
set -e

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install it first."
    exit 1
fi

if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install it first."
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "Creating .env file based on .env.example..."
    cp .env.example .env

    echo "Please enter your Telegram API credentials:"
    read -p "API_ID: " api_id
    read -p "API_HASH: " api_hash
    read -p "HANDLER (e.g., .saveit): " handler

    # Update .env file
    echo "API_ID_1=$api_id" > .env
    echo "API_HASH_1=$api_hash" >> .env
    echo "HANDLER=$handler" >> .env
fi

pip install --upgrade telethon python-dotenv pillow

echo "Running Saveit.py..."
python3 Saveit.py

echo "Done."