import sqlite3

conn = sqlite3.connect("database2.db")  # Ensure this is the correct database file
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:", tables)

conn.close()
