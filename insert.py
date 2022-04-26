from sql_commands import INSERT_QUERY

def get_insert_query():
    return INSERT_QUERY

def insert_data(connection, data: list):
    cursor = connection.cursor()

    insert = get_insert_query()

    for value in data:
        cursor.execute(insert, value)
    connection.commit()