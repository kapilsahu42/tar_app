import sqlite3

conn=sqlite3.connect('data.db')
course = conn.cursor()

create_table = " CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)"
course.execute(create_table)

conn.commit()
conn.close()