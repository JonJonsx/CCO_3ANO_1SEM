# encoding: iso-8859-1
from mysql.connector import connect as connect_my

from sql_commands import (CREATE_QUERY, DATABASE, DB_HOST, DB_PASSWORD,
                          DB_USER, DELETE_QUERY, SELECT_QUERY)


def get_connection():
    return connect_my(
        # host = DB_HOST + ":" + DB_PORT,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DATABASE
    )


def create_db():
    con = get_connection()
    c = con.cursor()
    c.execute(CREATE_QUERY)
    return con


def select_db(cursor):
    cursor.execute(SELECT_QUERY)
    return cursor.fetchall()


def truncate_table_db(cursor):
    cursor.execute(DELETE_QUERY)
