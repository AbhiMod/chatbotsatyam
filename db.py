from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import *
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
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5894209648:AAF1waPORM1VIJ_J7XSTywlVf7JOoKOoBIU") 
AMBOT = "6204761408"
BOT_USERNAME = os.environ.get("BOT_USERNAME","Defulter4_bot")
BOT_NAME = os.environ.get("BOT_NAME","Tisha")

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

# Connect to MongoDB
MONGO_URL = "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "VickDb"
mongo_client = MongoClient(MONGO_URL)
db = mongo_client[DATABASE_NAME]

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

# Handler for new chat members to collect group IDs
@bot.on_chat_member_updated()
async def chat_member_updated(client, message):
    # Check if the update is due to a new member joining
    if message.new_chat_member and message.new_chat_member.user.id == (await bot.get_me()).id:
        # Get the group chat ID
        chat_id = message.chat.id

        # Check if the group already exists in the database
        if not db["groups"].find_one({"chat_id": chat_id}):
            # If not, add the group to the database
            db["groups"].insert_one({"chat_id": chat_id})
EMOJIOS = [ 
      "═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══",
]
# Start command to collect users
@bot.on_message(filters.command(["start"]))
async def start_command(client, message):
    # Get user ID
    user_id = message.from_user.id

    # Check if the user already exists in the database
    if not db["users"].find_one({"user_id": user_id}):
        # If not, add the user to the database
        db["users"].insert_one({"user_id": user_id})

    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(0.1)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪")
    await asyncio.sleep(0.1)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║\n║\n║\n║\n║\n║")
    await asyncio.sleep(0.1)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║\n║\n║\n║\n║\n║\n╚══════ஜ۩۞۩ஜ═════╝")
    await asyncio.sleep(0.1)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║➣\n║\n║➣\n║\n║➣\n║\n╚══════ஜ۩۞۩ஜ═════╝")
    await asyncio.sleep(0.2)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║➣ @AMBOTYT\n║\n║➣\n║\n║➣\n║\n╚══════ஜ۩۞۩ஜ═════╝")
    await asyncio.sleep(0.2)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║➣ @AMBOTYT\n║\n║➣ @AM_YTSUPPORT\n║\n║➣\n║\n╚══════ஜ۩۞۩ஜ═════╝")
    await asyncio.sleep(0.2)
    await accha.edit("╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║➣ @AMBOTYT\n║\n║➣ @AM_YTSUPPORT\n║\n║➣ @satyamnetwork\n║\n╚══════ஜ۩۞۩ஜ═════╝")
     

# Command to send a broadcast to all users and groups
@bot.on_message(filters.command(["gcast"]))
async def broadcast_command(client, message):
    # Check if the sender is authorized to send broadcasts
    if str(message.from_user.id) == AMBOT:
        # Get the message content after the command
        text = message.text.split(maxsplit=1)[1]

        # Get all users and groups from the database
        users = db["users"].find()
        groups = db["groups"].find()

        # Initialize counts
        success_user_count = 0
        fail_user_count = 0
        success_group_count = 0
        fail_group_count = 0

        # Send the broadcast message to users
        for user in users:
            try:
                await bot.send_message(user["user_id"], text)
                success_user_count += 1
            except Exception as e:
                print(f"Error broadcasting to user {user['user_id']}: {str(e)}")
                fail_user_count += 1

        # Send the broadcast message to groups
        for group in groups:
            try:
                await bot.send_message(group["chat_id"], text)
                success_group_count += 1
            except Exception as e:
                print(f"Error broadcasting to group {group['chat_id']}: {str(e)}")
                fail_group_count += 1

        response_text = (
            f"Broadcast Successfull\n"
            f"Users : {success_user_count}\n"
            f"Groups : {success_group_count}\n"
            f"Failed Broadcast\n"
            f"Users : {fail_user_count}\n"
            f"Groups : {fail_group_count}"
        )

        await message.reply_text(response_text)
    else:
        await message.reply_text("You are not authorized to use this command.")

# Command to get statistics
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

    
print("Bot Is Alive")
# Run the bot
bot.run()
