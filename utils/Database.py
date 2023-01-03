from .Connection import DataBaseConnection

def CreateBookTable():
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def AddBook(name, author):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))

def GetAllBooks():
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM books ORDER BY author')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row  in cursor.fetchall()]
    return books

def MarkAsRead(name):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE books SET read=1 WHERE name=?', (name,))

def DeleteBook(name):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM books WHERE name=?', (name,))