import sqlite3


"""
def get_connection():
    conn = sqlite3.connect('base.db')
    return conn
"""

class ConnectionFactory:

    def get_connection(self):
        conn = sqlite3.connect('base.db')
        return conn
