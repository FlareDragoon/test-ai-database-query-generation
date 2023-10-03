from db import create_connection

def select_all_from_games(conn):
    """
    Query all rows in the games table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM games")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_from_table(conn, query):
    """
    Query rows based on the provided query
    :param conn: the Connection object
    :param query: SQL query to be executed
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    database = "./pythonsqlite.db"
    conn = create_connection(database)

    query = input("Please enter your query: ")
    print(f"Executing query: {query}")
    select_from_table(conn, query)
