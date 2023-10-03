import os

from db import create_table, create_connection
from schema import *

def select_all_from_games(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM games")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_to_genres(conn):
    sql = """
        INSERT INTO genres VALUES
	    (1, 'Action'),
        (2, 'Adventure'),
        (3, 'RPG'),
        (4, 'Simulation');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_platforms(conn):
    sql = """
        INSERT INTO platforms VALUES
        (1, 'PC'),
        (2, 'PS5'),
        (3, 'Xbox X'),
        (4, 'Switch'),
        (5, 'Multiple'),
        (6, 'PS4');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_studios(conn):
    sql = """
        INSERT INTO studios VALUES
        (1, 'Nintendo', 'Kyoto'),
        (2, 'Guerrilla Games', 'Amsterdam'),
        (3, 'Sonic Team', 'Tokyo'),
        (4, 'BlueTwelve Studio', 'Montpellier'),
        (5, 'Square Enix', 'Tokyo'),
        (6, 'EA', 'California'),
        (7, 'Insomniac Games', 'California');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_games(conn):
    sql = """
        INSERT INTO games VALUES
        (1, 'Final Fantasy XVI', 2023, 5, 2, 3),
        (2, 'Final Fantasy VII: Rebirth', 2024, 5, 2, 3),
        (3, 'Star Wars Jedi: Survivor', 2023, 6, 2, 2),
        (4, 'The Legend of Zelda: Tears of the Kingdom', 2023, 1, 4, 2),
        (5, 'Stranger of Paradise: Final Fantasy Origin', 2022, 5, 5, 3),
        (6, 'Spider-Man 2', 2023, 7, 2, 1),
        (7, 'Spider-Man: Miles Morales', 2020, 7, 2, 1),
        (8, 'Crisis Core: Final Fantasy VII Reunion', 2022, 5, 5, 3),
        (9, 'The Legend of Zelda: Breath of the Wild', 2017, 1, 4, 2),
        (10, 'Dragon Quest Monsters: The Dark Prince', 2023, 5, 4, 3),
        (11, 'Horizon: Forbidden West', 2022, 2, 2, 1),
        (12, 'Sonic Frontiers', 2022, 3, 5, 2),
        (13, 'Stray', 2022, 4, 5, 1),
        (14, 'Horizon: Zero Dawn', 2017, 2, 6, 1);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_characters(conn):
    sql = """
        INSERT INTO characters VALUES
        (1, 'Clive Rosfield', 1),
        (2, 'Jill Warrick', 1),
        (3, 'Cloud', 2),
        (4, 'Tifa', 2),
        (5, 'Cal Kestis', 3),
        (6, 'Garland', 5),
        (7, 'Zach', 8),
        (8, 'Yuffie', 2),
        (9, 'Peter Parker', 6),
        (10, 'Mary Jane Watson', 6),
        (11, 'Miles Morales', 7),
        (12, 'Psaro', 10),
        (13, 'Aloy', 11),
        (14, 'Sonic', 12),
        (15, 'B12', 13),
        (16, 'Link', 9);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_character_games(conn):
    #id, characterid, gameid
    sql = """
        INSERT INTO character_games VALUES
        (1, 1, 1),
        (2, 3, 2),
        (3, 5, 3),
        (4, 16, 4),
        (5, 6, 5),
        (6, 9, 6),
        (7, 11, 7),
        (8, 7, 8),
        (9, 16, 9),
        (10, 12, 10),
        (11, 13, 11),
        (12, 14, 12),
        (13, 15, 13),
        (14, 13, 14)
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    
    create_table(conn, sql_create_genres_table)
    insert_to_genres(conn)
    
    create_table(conn, sql_create_platforms_table)
    insert_to_platforms(conn)
    
    create_table(conn, sql_create_studios_table)
    insert_to_studios(conn)
    
    create_table(conn, sql_create_games_table)
    insert_to_games(conn)
    
    create_table(conn, sql_create_characters_table)
    insert_to_characters(conn)
    
    create_table(conn, sql_create_character_games_table)
    insert_to_character_games(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()
