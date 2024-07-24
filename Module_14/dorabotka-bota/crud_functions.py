import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Product(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
        '''
    )
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Product')
    result = cursor.fetchall()
    connection.close()
    return result


def post_products():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute(
            "INSERT INTO Product (title, description, price) VALUES (?, ?, ?)",
            (f"Продукт {i}", f"описание {i}", i * 100)
        )
    connection.commit()
    connection.close()
