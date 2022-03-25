from ast import keyword
import asyncio
from datetime import date
from telethon import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

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
    i = 0 # Biến đếm số lượng tin nhắn tìm được
    x = 0 # Tháng của date1
    y = 1 # Tháng của date2
    xx = 2020 # Năm của date1
    yy = 2020 # Năm của date2
    while yy<=2022:
        if x == 12: 
            x=1
            xx+=1
        if y == 12: 
            y=1
            yy+=1
        x+=1
        y+=1
        result = await client(SearchRequest(
        peer=search_group,          # On which chat/conversation
        q=keyword_search,           # What to search for
        filter=filter,              # Filter to use (maybe filter for media)
        min_date=date(xx, x, 1),    # Minimum date
        max_date=date(yy, y, 1),    # Maximum date
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
        for index in result.messages:
            i+=1
            print(i, index.message)



with client:
    client.loop.run_until_complete(main())
