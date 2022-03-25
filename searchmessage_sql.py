from ast import keyword
import asyncio
from datetime import date
from telethon import TelegramClient
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
    search_group = 'BeInCrypto Việt Nam Community' #input("Nhập tên nhóm muốn tìm kiếm từ khoá: ")
    keyword_search = 'tăng' #input("Nhập từ khoá muốn tìm kiếm: ")
    filter = InputMessagesFilterEmpty()
    
    result = await client(SearchRequest(
    peer=search_group,          # On which chat/conversation
    q=keyword_search,           # What to search for
    filter=filter,              # Filter to use (maybe filter for media)
    min_date=None,              # Minimum date
    max_date=None,              # Maximum date
    offset_id=0,                # ID of the message to use as offset
    add_offset=0,               # Additional offset
    limit=120,                  # How many results
    max_id=0,                   # Maximum message ID
    min_id=0,                   # Minimum message ID
    hash=-1435215991210501094,  # access_hash in result.chats         
    from_id=None                # Who must have sent the message (peer)
    ))
    # f = open('myfile.txt',"w", encoding='utf-8')
    # f.write(result.stringify())
    
    filled = input("Nhập vào từ khoá tìm nhóm để search data: ")

    # Lấy dữ liệu nhập vào và chuyển thành tuple
    q = ()
    listq = list(q)
    listq.append(filled)
    q = tuple(listq)

    Q1 = "SELECT id_channel, gr_channel_names FROM gr_channels WHERE keyword=%s"
    cursor.execute(Q1, q)
    testfetch = cursor.fetchall()
    for index in result.messages:
        i+=1
        print(i, index.message)



with client:
    client.loop.run_until_complete(main())