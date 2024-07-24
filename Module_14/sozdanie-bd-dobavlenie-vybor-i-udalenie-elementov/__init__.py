import sqlite3
import os

sql_file = "not_telegram.db"

if os.path.isfile(sql_file):
    os.remove(sql_file)

connection = sqlite3.connect(sql_file)
cursor = connection.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
    '''
)

for i in range(1, 11):
    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, '1000')",
        (f"User{i}", f"example{i}@gmail.ru", i * 10)
    )

for i in range(1, 11, 2):
    cursor.execute(
        "UPDATE Users SET balance = ? WHERE id = ?",
        (500, i)
    )

for i in range(1, 11, 3):
    cursor.execute(
        "DELETE FROM Users WHERE id = ?", (i, )
    )

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for username, email, age, balance in users:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()
