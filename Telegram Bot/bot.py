from telebot.async_telebot import AsyncTeleBot
# dependencies
# pyTelegramBotAPI
# aiohttp
from dotenv import load_dotenv
import os
import asyncio
from bot_functions import input_data_to_database
from bot_functions import download_photo

load_dotenv()
token = os.getenv('BOT_KEY')
channel = os.getenv('CHANNEL_ID')
bot = AsyncTeleBot(token, parse_mode=None)

@bot.message_handler(content_types=['photo'])
async def get_photo(message):
    if message.caption:
        photo_name = input_data_to_database(message)
        
    if message.photo:
        link_to_download_photo = await bot.get_file_url(message.photo[-1].file_id)
        download_photo(link_to_download_photo, photo_name)

# Run until action break in terminal
asyncio.run(bot.infinity_polling())
