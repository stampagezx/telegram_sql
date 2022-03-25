import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
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

filled = input("Nhập vào từ khoá tìm nhóm để lấy data: ")

# Lấy dữ liệu nhập vào và chuyển thành tuple
q = ()
listq = list(q)
listq.append(filled)
q = tuple(listq)

# Query
Q1 = "SELECT id_channel, gr_channel_names FROM gr_channels WHERE keyword=%s"
Q2 = "INSERT INTO message (message_id, channel_id, content, create_at) VALUES (%s, %s, %s, %s)"
cursor.execute(Q1, q)
testfetch = cursor.fetchall()

async def main():
    for index in testfetch:
        print(index[0], index[1])
        async for message in client.iter_messages(index[0], limit=400):
            print(message.id, message.text)
            val = (message.id, index[0], message.message, message.date)
            cursor.execute(Q2, val)
            conn.commit()

    

with client:
    client.loop.run_until_complete(main())