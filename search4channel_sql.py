import asyncio
from telethon import TelegramClient
from telethon import functions, types
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

Q1 = "SELECT search_channel_names FROM gr_keywords"
cursor.execute(Q1)
testfetch = cursor.fetchall()

for index in testfetch:
    print(index[0])

async def main(): 
    for index in testfetch:
        search = index[0]
        print(index[0])
        result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
        for index in result.chats:
            print(index.id, index.title)
            cursor.execute("INSERT INTO gr_channels (id_channel, type, keyword, gr_channel_names) VALUES (%s, %s, %s, %s)", (index.id, index.megagroup, search, index.title))
            cursor.fetchone()
            conn.commit()

with client:
    client.loop.run_until_complete(main())
