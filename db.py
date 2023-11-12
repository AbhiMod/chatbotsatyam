from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import *
from pyrogram.types import InputMediaPhoto
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime
# Initialize Pyrogram client
API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6684745377:AAFT0sUF1QlIyBlR09ekxSggdon9FxFcT_A") 
AMBOT = ["6204761408", ""]
AM = ["6204761408", ""]
BOT_USERNAME = os.environ.get("BOT_USERNAME","Tisha_machine_bot")
BOT_NAME = os.environ.get("BOT_NAME","𝙼𝚒𝚜𝚜 𝚃𝚒𝚜𝚑𝚊 💞")
MONGO_URL = "mongodb+srv://MissTisha:MissTisha@misstisha.eatdvt1.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "MissTisha"
mongo_client = MongoClient(MONGO_URL)
db = mongo_client[DATABASE_NAME]
START_PHOTOS = [
    "https://graph.org/file/be8d60272e859df723cbb.jpg",
    "https://graph.org/file/252742c9f9dfe1c056894.jpg",
    "https://graph.org/file/c0c800c2e4a5b72533691.jpg",
    "https://graph.org/file/6a13cf043845b927e8cb2.jpg",
    "https://graph.org/file/1f7906f11316e5685b112.jpg",
]

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]
@bot.on_chat_member_updated()
async def chat_member_updated(client, message):
    if message.new_chat_member and message.new_chat_member.user.id == (await bot.get_me()).id:
        # Get the group chat ID
        chat_id = message.chat.id
        if not db["groups"].find_one({"chat_id": chat_id}):
            # If not, add the group to the database
            db["groups"].insert_one({"chat_id": chat_id})

@bot.on_message(filters.command(["start"]))
async def start_command(client, message):
    # Get user ID
    user_id = message.from_user.id
    if not db["users"].find_one({"user_id": user_id}):
        db["users"].insert_one({"user_id": user_id})
    ambot_op = random.choice(START_PHOTOS)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ 💞", url="https://t.me/satyamnetwork"),
         InlineKeyboardButton("💌 ᴄʜᴀᴛ ɢʀᴏᴜᴘ", url="https://t.me/+eSTzpugepEMwNDBl")],
        [InlineKeyboardButton(" ʜᴇʟᴘ ", callback_data="help")]
    ])
    await message.reply_photo(
        photo=ambot_op,
        caption=f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}

➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.
➻ {BOT_NAME} ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.
➻ {BOT_NAME} ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.
➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.
➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴩ.
        """,
        reply_markup=keyboard
    )
@bot.on_callback_query(filters.regex("^help$"))
async def help_callback(client, callback_query):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(" ʙᴀᴄᴋ ", callback_data="back")]
    ])
    await callback_query.message.edit_text(""" 
➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]
➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) 
➻ ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ
➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴩ ᴀɴᴅ ᴀʙᴏᴜᴛ [ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://t.me/AM_YTBOTT)
""", reply_markup=keyboard)
@bot.on_callback_query(filters.regex("^back$"))
async def back_callback(client, callback_query):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ 💞", url="https://t.me/satyamnetwork"),
         InlineKeyboardButton("💌 ᴄʜᴀᴛ ɢʀᴏᴜᴘ", url="https://t.me/+eSTzpugepEMwNDBl")],
        [InlineKeyboardButton(" ʜᴇʟᴘ ", callback_data="help")]
    ])
    await callback_query.message.edit_text(f"""" 
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.
➻ {BOT_NAME} ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.
➻ {BOT_NAME} ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.
➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.
➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴩ ᴀɴᴅ ᴀʙᴏᴜᴛ [ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](t.me/AM_YTBOTT)
""", reply_markup=keyboard)
@bot.on_message(filters.command(["help"]))
async def help_command(client, message):
    # Get user ID
    user_id = message.from_user.id
    # Check if the user already exists in the database
    if not db["users"].find_one({"user_id": user_id}):
        # If not, add the user to the database
        db["users"].insert_one({"user_id": user_id})
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ],
        [
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ 💞", url="https://t.me/satyamnetwork"),
            InlineKeyboardButton("💌 ᴄʜᴀᴛ ɢʀᴏᴜᴘ", url="https://t.me/+eSTzpugepEMwNDBl"),
        ],
        [InlineKeyboardButton(" ʜᴇʟᴘ ", callback_data="help")]
    ])
    await message.reply_text(f""" 
ʜᴇʀᴇ ɪꜱ ʙᴏᴛ ᴄᴍᴅꜱ

➻  /stats - ʙᴏᴛ ꜱᴛᴀᴛꜱ
➻  /gcast - ʙʀᴏᴀᴅᴄᴀꜱᴛ 
➻  /chatbot - [ᴏɴ/ᴏғғ]
➻ /sudolist - ʙᴏᴛ ꜱᴜᴅᴏʟɪꜱᴛ
➻ /addsudo - ᴀᴅᴅ ᴛᴏ ꜱᴜᴅᴏ
➻ /repo - ɢᴇᴛ ʙᴏᴛ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
""", reply_markup=keyboard)
@bot.on_message(filters.command(["addsudo"]))
async def addsudo_command(client, message):
    # Check if the sender is the bot owner
    if str(message.from_user.id) == AM[0]:
        # Get the user ID from the command message
        command_parts = message.text.split(maxsplit=1)
        if len(command_parts) < 2:
            await message.reply_text("Invalid usage. Please provide a user ID to add.")
            return
        user_id = command_parts[1]
        AMBOT.append(user_id)
        global bot
        bot.AMBOT = AMBOT
        await message.reply_text(f"User {user_id} added to the sudo users list.")
    else:
        await message.reply_text("You are not sudo user to use this command.")
# Command to get the list of sudo users and owners
@bot.on_message(filters.command(["sudolist"]))
async def sudolist_command(client, message):
    # Check if the sender is authorized to view the sudo list
    if str(message.from_user.id) in AMBOT:
        # Prepare the list of sudo users
        sudo_list = "\n".join([f"{index + 1}. {user_id}" for index, user_id in enumerate(AMBOT)])
        owner_list = "\n".join([f"{index + 1}. {user_id}" for index, user_id in enumerate(AM)])
        response_text = (
            f"👑 Owner :\n{owner_list}\n\n"
            f"🔥 Sudo Users:\n{sudo_list}"
        )

        await message.reply_text(response_text)
    else:
        await message.reply_text("You are not Auth to use this command.")
@bot.on_message(filters.command(["repo"]))
async def repo_command(client, message):
    random_photo = random.choice(START_PHOTOS)
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/AM_YTBOTT")]])
    await message.reply_photo(random_photo, caption="ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴛʜᴇ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ.", reply_markup=keyboard)
@bot.on_message(filters.command(["gcast"]))
async def broadcast_command(client, message):
    # Check if the sender is authorized to send broadcasts
    if str(message.from_user.id) in AMBOT:
        # Get the message content after the command
        command_parts = message.text.split(maxsplit=1)
        if len(command_parts) < 2:
            await message.reply_text("Invalid usage. Please provide a message to broadcast.")
            return
        text = command_parts[1]
        users = db["users"].find()
        groups = db["groups"].find()
        success_user_count = 0
        fail_user_count = 0
        success_group_count = 0
        fail_group_count = 0
        for user in users:
            try:
                await bot.send_message(user["user_id"], text)
                success_user_count += 1
            except Exception as e:
                print(f"Error broadcasting to user {user['user_id']}: {str(e)}")
                fail_user_count += 1
        for group in groups:
            try:
                await bot.send_message(group["chat_id"], text)
                success_group_count += 1
            except Exception as e:
                print(f"Error broadcasting to group {group['chat_id']}: {str(e)}")
                fail_group_count += 1
        response_text = (
            f"Broadcast Successful\n"
            f"Users : {success_user_count}\n"
            f"Groups : {success_group_count}\n"
            f"Failed Broadcast\n"
            f"Users : {fail_user_count}\n"
            f"Groups : {fail_group_count}"
        )
        await message.reply_text(response_text)
    else:
        await message.reply_text("You are not owner to use this command.")
@bot.on_message(filters.command(["stats"]))
async def stats_command(client, message):
    # Get counts
    user_count = db["users"].count_documents({})
    group_count = db["groups"].count_documents({})
    response_text = (
        f"Bot Stats\n"
        f"Total Users : {user_count}\n"
        f"Total Groups : {group_count}"
    )
    await message.reply_text(response_text)
print("AMBot Is Alive")
bot.run()
