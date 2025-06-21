import os
import sys
import asyncio
import logging
import pandas as pd
from telethon import TelegramClient
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("TelegramMessageFetcher")

# Load environment variables
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("api_id")
API_HASH = os.getenv("api_hash")

if not API_ID or not API_HASH:
    logger.error("API ID or API Hash not found. Please check your .env file.")
    sys.exit("Error: Missing credentials in .env file.")

# Channels to fetch messages from
CHANNEL_USERNAMES = [
    "@ZemenExpress",
    "@Fashiontera",
    "@nevacomputer",
    "@ethio_brand_collection",
    "@Shewabrand",
    
]

# Output file path
OUTPUT_FILE = "../data/Scraping data.csv"


async def fetch_messages(client, channel_username, limit=100):
    """
    Fetch messages from a given Telegram channel.
    
    Args:
        client (TelegramClient): The Telegram client.
        channel_username (str): The username of the Telegram channel.
        limit (int): The number of messages to fetch.
    
    Returns:
        list: A list of message texts from the channel.
    """
    logger.info(f"Fetching messages from channel: {channel_username}")
    try:
        messages = [message.text for message in await client.iter_messages(channel_username, limit=limit)]
        logger.info(f"Fetched {len(messages)} messages from {channel_username}")
        return messages
    except Exception as e:
        logger.error(f"Error fetching messages from {channel_username}: {e}")
        return []


async def save_messages_to_csv(messages, file_path):
    """
    Save messages to a CSV file.

    Args:
        messages (list): A list of messages.
        file_path (str): The path to save the CSV file.
    """
    if os.path.exists(file_path):
        choice = input(f"File {file_path} already exists. Do you want to override it? (Y/N): ").strip().lower()
        if choice != "y":
            logger.info("Operation cancelled.")
            return

    df = pd.DataFrame(messages, columns=["messages"])
    df.to_csv(file_path, index=False)
    logger.info(f"Messages saved to {file_path}")


async def main():
    """
    Main function to fetch and save messages from Telegram channels.
    """
    logger.info("Initializing Telegram client...")
    async with TelegramClient("session_name", API_ID, API_HASH) as client:
        logger.info("Telegram client connected successfully.")
        logger.info(f"Starting to fetch messages from {len(CHANNEL_USERNAMES)} channels...")

        # Fetch messages from all channels
        tasks = [fetch_messages(client, username) for username in CHANNEL_USERNAMES]
        results = await asyncio.gather(*tasks)

        # Filter out errors and flatten the list of messages
        all_messages = [msg for sublist in results if sublist for msg in sublist]
        logger.info(f"Fetched a total of {len(all_messages)} messages.")

        if all_messages:
            await save_messages_to_csv(all_messages, OUTPUT_FILE)
        else:
            logger.warning("No messages fetched. No file will be created.")


if __name__ == "__main__":
    asyncio.run(main())