import telebot
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os
import asyncio
# Run this script once only, or every time the command list need to be updated

load_dotenv()
BOT_KEY = 'BOT_KEY'
EX_BOT_KEY = 'EXPERIMENTAL_BOT_KEY'
ADMIN_GROUP_ID = 'EXPERIMENTAL_GROUP_ID'

token = os.getenv(BOT_KEY)
admin_group = os.getenv(ADMIN_GROUP_ID)

bot = AsyncTeleBot(token, parse_mode=None)

async def main():
    await bot.delete_my_commands()
    
    admin_commands = {
        telebot.types.BotCommand("addroute", "Add a route to the database"),
        telebot.types.BotCommand("changeroute", "Fix a route in the database"),
        telebot.types.BotCommand("deleteroute", "Delete a route using name")        
    }
    
    admin_scope = telebot.types.BotCommandScopeChatAdministrators(chat_id=admin_group)
    
    await bot.set_my_commands(commands=admin_commands, scope=admin_scope)
    
    confirm_commands_exist = await bot.get_my_commands(scope=admin_scope, language_code=None)
    print("Number of commands added: " + str(len(confirm_commands_exist)))
    
asyncio.run(main())
