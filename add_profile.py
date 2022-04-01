from ast import keyword
import asyncio
import re
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "tutorialbase"
)

cursor = conn.cursor()

with open('api_id.txt', 'r') as f1:
    api_id = f1.read()
with open('api_hash.txt', 'r') as f2:
    api_hash = f2.read()

client = TelegramClient('user', api_id, api_hash)
client.start()

async def main():

    filter = InputMessagesFilterEmpty()

    Q1 = "SELECT channel_username FROM gr_channel_handmade"
    Q2 = "UPDATE gr_channel_handmade SET id_channel = %s, access_hashh = %s  WHERE channel_username = %s"

    cursor.execute(Q1)
    fetch1 = cursor.fetchall()
    for item in fetch1:
        result = await client(functions.channels.GetChannelsRequest(
        id=[item[0]]
        ))
        cursor.execute(Q2, (result.chats[0].id, result.chats[0].access_hash, item[0]))
        conn.commit()
with client:
    client.loop.run_until_complete(main())