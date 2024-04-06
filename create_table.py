import sqlite3

def create_table ():
    conn = sqlite3.connect('user_db.db')

    cursor = conn.cursor()

    create_table_query = '''CREATE TABLE users( 
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INT,
        gender TEXT,
        address TEXT
    )
    '''

    cursor.execute(create_table_query)

    conn.commit()


