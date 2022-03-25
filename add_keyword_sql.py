import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "tutorialbase"
)

cursor = conn.cursor()
id = 0
while True:
    id += 1
    keywordgg = input("Nhập từ khoá tìm kiếm vào database: ")
    cursor.execute("INSERT INTO gr_keywords (id, search_channel_names) VALUES (%s, %s)", (id, keywordgg))
    conn.commit()