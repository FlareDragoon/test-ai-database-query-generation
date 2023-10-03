sql_create_genres_table = """
    CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    genre_name TEXT
    );
"""

sql_create_games_table = """
    CREATE TABLE games (
        game_id INT PRIMARY KEY,
        title TEXT,
        release_year INT,
        studio_id INT,
        platform_id INT,
        genre_id INT,
        FOREIGN KEY (studio_id) references studios(studio_id)
        FOREIGN KEY (platform_id) references platforms(platform_id),
        FOREIGN KEY (genre_id) references genres(genre_id)
    );
"""

sql_create_platforms_table = """
    CREATE TABLE platforms (
    platform_id INT PRIMARY KEY,
    platform_name TEXT
    );
"""

sql_create_studios_table = """
    CREATE TABLE studios (
        studio_id INT PRIMARY KEY,
        studio_name TEXT,
        studio_location TEXT
        );  
"""

sql_create_characters_table = """
    CREATE TABLE characters (
        character_id INT PRIMARY KEY,
        character_name TEXT,
        game_id INT,
        FOREIGN KEY (game_id) references games(game_id)
    );
"""

sql_create_character_games_table = """
    CREATE TABLE character_games (
        character_game_id INT PRIMARY KEY,
        character_id INT,
        game_id INT,
        FOREIGN KEY (character_id) references characters(character_id),
        FOREIGN KEY (game_id) references games(game_id)
    );
"""

def get_schema():
    schema = f"{sql_create_genres_table}{sql_create_games_table}{sql_create_platforms_table}{sql_create_studios_table}{sql_create_characters_table}{sql_create_character_games_table}"
    return schema
