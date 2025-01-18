import sqlite3

class Database: 
    def __init__(self, db_name='library.db'):
      self.connection = sqlite3.connect(db_name)
      self.create_tables()

    def create_tables(self):
      with self.connection:
        with self.connection:
          