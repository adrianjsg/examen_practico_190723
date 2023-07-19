import sqlite3

def create_database():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

    return connection

def close_database(connection):
    connection.close()
