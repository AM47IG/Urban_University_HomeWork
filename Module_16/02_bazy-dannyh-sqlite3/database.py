import sqlite3


def check_has_db_and_create(name):
    func_work_with_db(name)(
        '''
        CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS Grades(
        id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        grade FLOAT NOT NULL,
        FOREIGN KEY(student_id) REFERENCES Students(id))
        '''
    )


def func_work_with_db(name):
    def wrapper(*executes):
        result = []
        connection = sqlite3.connect(f"{name}.db")
        cursor = connection.cursor()
        for execute in executes:
            cursor.execute(execute)
            if execute.strip().startswith('SELECT'):
                for el in cursor.fetchall():
                    result.append(el)
        connection.commit()
        connection.close()
        return result
    return wrapper


func_work_with_db('Urban')('DELETE FROM Students', 'DELETE FROM Grades')  # Очистка базы. Надоело удалять вручную...
