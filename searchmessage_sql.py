from ast import keyword
import asyncio
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

    filled = 'crypto' # input("Nhập vào từ khoá tìm nhóm để search data: ")
    filter = InputMessagesFilterEmpty()

    # Lấy dữ liệu nhập vào và chuyển thành tuple
    q = ()
    listq = list(q)
    listq.append(filled)
    q = tuple(listq)

    Q1 = "SELECT id_channel, access_hashh, gr_channel_names FROM gr_channels WHERE keyword=%s"
    Q2 = "INSERT INTO search_message_bykeyword (message_id, keyword_search, channel_id, content, create_at) VALUES (%s, %s, %s, %s, %s)"
    Q3 = "SELECT searchKeyword FROM msg_keywords"

    cursor.execute(Q1, q)
    testfetch = cursor.fetchall()
    cursor.execute(Q3)
    fetch2 = cursor.fetchall()
    for keyword_search in fetch2:
        for index in testfetch:
            print(index[2])
            access_hashh=int(index[1])
            result = await client(SearchRequest(
            peer=str(index[2]),         # On which chat/conversation
            q=keyword_search[0],           # What to search for
            filter=filter,              # Filter to use (maybe filter for media)
            min_date=None,              # Minimum date
            max_date=None,              # Maximum date
            offset_id=0,                # ID of the message to use as offset
            add_offset=0,               # Additional offset
            limit=120,                  # How many results
            max_id=0,                   # Maximum message ID
            min_id=0,                   # Minimum message ID
            hash= access_hashh,         # access_hash in result.chats         
            from_id=None                # Who must have sent the message (peer)
            ))

            # print(result.stringify()) #Try to get form of result
            i=0
            for index1 in result.messages:
                i+=1
                print(i, index1.message)
                val = (index1.id, keyword_search[0], index[0], index1.message, index1.date)
                cursor.execute(Q2, val)
                cursor.fetchone()
                conn.commit()
        
with client:
    client.loop.run_until_complete(main())
