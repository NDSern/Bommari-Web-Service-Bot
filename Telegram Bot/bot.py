from telebot.async_telebot import AsyncTeleBot
# dependencies
# pyTelegramBotAPI
# aiohttp
from dotenv import load_dotenv
import os
import asyncio
from bot_functions import input_data_to_database
from bot_functions import download_photo
from bot_functions import check_for_valid_format
from bot_functions import change_route
from bot_functions import delete_route
from bot_functions import update_route

load_dotenv()
BOT_KEY = 'BOT_KEY'
EX_BOT_KEY = 'EXPERIMENTAL_BOT_KEY'

token = os.getenv(BOT_KEY)
channel = os.getenv('CHANNEL_ID')
bot = AsyncTeleBot(token, parse_mode=None)

@bot.message_handler(content_types=['photo'])
async def get_photo(message):
    route_name = message.caption
    
    # Check whether or not route name has followed a format
    if not route_name or not message.photo:
        print("Route has no name or photo!")
        reply_message = await bot.reply_to(message, "Please use the correct format in the pinned message.")
        await asyncio.sleep(3600)
        await bot.delete_message(reply_message.chat.id, reply_message.message_id)
        return False
    
    if not check_for_valid_format(route_name):
        print("Wrong format!")
        reply_message = await bot.reply_to(message, "Please use the correct format in the pinned message.")
        await asyncio.sleep(3600)
        await bot.delete_message(reply_message.chat.id, reply_message.message_id)
        return False

    # Adding to database
    photo_name = input_data_to_database(message)
    
    # Downloading photo from Telegram
    link_to_download_photo = await bot.get_file_url(message.photo[-1].file_id)
    download_photo(link_to_download_photo, photo_name)

@bot.edited_message_handler(content_types=['photo'])
async def get_edited_photo(message):
    update_route(message)        
    await get_photo(message)
    
@bot.message_handler(commands=['addroute'])
async def command_asd(message):
    if not await get_photo(message.caption[9:].strip()):
        await bot.reply_to(message, "Wrong format!")
        return False
    
    print("Admin command add route successfully!")
    await bot.reply_to(message, "Route added successfully!")
    
@bot.message_handler(commands=["changeroute"])
async def command_change_route(message):
    wrong_format_message = "Format is \"/changeroute <initial route name> | <fixed route name>\""
    if not message.text:
        print("Admin command change route need text.")
        await bot.reply_to(message, wrong_format_message)
        return False

    if not change_route(message.text):
        await bot.reply_to(message, "Change unsuccessful!")
    else:
        await bot.reply_to(message, "Changed successful!")
        
@bot.message_handler(commands=["deleteroute"])
async def command_delete_route(message):
    if not message.text:
        print("Admin command delete route need text.")
        await bot.reply_to(message, "Format is \"/changeroute <initial route name> | <fixed route name>\"")
        return False

    if not delete_route(message.text):
        await bot.reply_to(message, "Change unsuccessful!")
    else:
        await bot.reply_to(message, "Changed successful!")
        
        
asyncio.run(bot.infinity_polling())
