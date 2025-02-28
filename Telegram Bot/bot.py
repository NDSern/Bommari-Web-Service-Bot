from telebot.async_telebot import AsyncTeleBot
# dependencies
# pyTelegramBotAPI
# aiohttp
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()
token = os.getenv('BOT_KEY')
channel = os.getenv('CHANNEL_ID')
bot = AsyncTeleBot(token, parse_mode=None)

@bot.channel_post_handler(func=lambda message:True)
async def get_channel_message_update(message):
    await bot.reply_to(message, message.text)

# Testing: echo all messages
# @bot.message_handler(func=lambda message:True)
# async def get_message_update(message):
#     await bot.reply_to(message, message)    

# Run until action break in terminal
asyncio.run(bot.infinity_polling())
