# encoding: iso-8859-1
from create import create_db, select_db, truncate_table_db
from insert import insert_data


class DatabaseManager:
    def __init__(self):
        self.connection = self.create()
        self.cursor = None

    def create(self):
        return create_db()

    def select(self) -> list:
        return select_db(cursor=self.connection.cursor())

    def insert(self, dados: list):
        insert_data(self.connection, dados)

    # def select(self) -> list:
    #     return select_data(cursor=self.connection.cursor())

    def truncate_table(self):
        truncate_table_db(cursor=self.connection.cursor())
