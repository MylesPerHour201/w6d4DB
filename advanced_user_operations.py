import sqlite3
from create_table import create_table

class AdvancedUserOperations:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('user-db.db')
        self.cursor = self.conn.cursor()
        table = '''CREATE TABLE users( 
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INT,
        gender TEXT,
        address TEXT
        )
        '''
        self.cursor.execute(table)

    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
        self.cursor.execute('''
                            INSERT INTO users (username, email, password, age, gender, address) 
                            VALUES (?, ?, ?, ?, ?, ?)''', (name, email, password, age, gender, address))
        self.conn.commit()

 

    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):
        query = 'SELECT * FROM users WHERE 1=1 '
        parameters = []
        
        if min_age is not None:
            query += 'AND age >= ? '
            parameters.append(min_age)
        if max_age is not None:
            query += 'AND age <= ? '
            parameters.append(max_age)
        if gender is not None:
            query += 'AND gender = ? '
            parameters.append(gender)
        
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def update_user_profile(self, email, age=None, gender=None, address=None):
        update_query = 'UPDATE users SET '
        parameters = []
        
        if age is not None:
            update_query += 'age = ?, '
            parameters.append(age)
        if gender is not None:
            update_query += 'gender = ?, '
            parameters.append(gender)
        if address is not None:
            update_query += 'address = ?, '
            parameters.append(address)
        
        update_query = update_query.rstrip(', ') + ' WHERE email = ?'
        parameters.append(email)
        
        self.cursor.execute(update_query, parameters)
        self.conn.commit()

 

    def delete_users_by_criteria(self, gender=None):
        if gender is not None:
            self.cursor.execute('DELETE FROM users WHERE gender = ?', (gender,))
            self.conn.commit()

 

    def __del__(self):

        self.conn.close()

 