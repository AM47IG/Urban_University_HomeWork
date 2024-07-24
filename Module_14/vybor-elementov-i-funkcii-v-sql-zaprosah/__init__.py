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

cursor.execute("DELETE FROM Users WHERE id = 6")
cursor.execute("SELECT count(username) FROM Users")
count = cursor.fetchone()[0]
cursor.execute("SELECT sum(balance) FROM Users")
summ = cursor.fetchone()[0]
print(summ / count)


connection.commit()
connection.close()
