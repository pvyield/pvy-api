import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Database:
    @classmethod
    def create_db(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        cursor.execute(create_table)

        insert_query = "INSERT INTO users (username, password) VALUES (?, ?)"

        users = [
            ('bob', 'asdf'),
            ('rolf', 'asdf'),
            ('anne', 'xyz')
        ]
        cursor.executemany(insert_query, users)

        create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
        cursor.execute(create_table)

        connection.commit()
        connection.close()
