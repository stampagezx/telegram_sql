from sqlite3 import Cursor
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "tutorialbase"
)

cursor = conn.cursor()

Q1 = "CREATE TABLE gr_keywords (id int PRIMARY KEY, search_channel_names VARCHAR(80) NOT NULL)"
Q2 = "CREATE TABLE msg_keywords (id int PRIMARY KEY AUTO_INCREMENT, searchKeyword VARCHAR(50) NOT NULL)"
Q3 = "CREATE TABLE gr_channels (id int PRIMARY KEY AUTO_INCREMENT, type BIT NOT NULL, id_channel int, keyword VARCHAR(50),access_hashh VARCHAR(50), gr_channel_names VARCHAR(50) NOT NULL)"
Q4 = "CREATE TABLE message (id int PRIMARY KEY AUTO_INCREMENT, message_id int, channel_id int, content VARCHAR(8000), create_at DATE)"
Q5 = "CREATE TABLE search_message_bykeyword (id int PRIMARY KEY AUTO_INCREMENT, message_id int, keyword_search VARCHAR(100), channel_id int, content VARCHAR(8000), create_at DATE)"

cursor.execute(Q1)
cursor.execute(Q2)
cursor.execute(Q3)
cursor.execute(Q4)
cursor.execute(Q5)

