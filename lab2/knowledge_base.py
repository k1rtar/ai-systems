
from pyswip import Prolog

def load_knowledge_base():
    """
    Загружает базу знаний Prolog из внешнего файла .pl.
    """
    prolog = Prolog()
    prolog.consult("videogames.pl")
    return prolog

def is_valid_genre(prolog, genre):
    query = f"genre({genre})"
    return bool(list(prolog.query(query)))

def is_valid_platform(prolog, platform):
    query = f"platform({platform})"
    return bool(list(prolog.query(query)))

def is_valid_developer(prolog, developer):
    query = f"developer({developer})"
    return bool(list(prolog.query(query)))

def query_games_by_genres(prolog, genres):
    games = set()
    for genre in genres:
        query = f"game_genre(Game, {genre})"
        result = list(prolog.query(query))
        for r in result:
            games.add(r["Game"])
    return games

def query_games_by_developer(prolog, developer):
    query = f"game_developer(Game, {developer})"
    result = list(prolog.query(query))
    return [r["Game"] for r in result]

def query_game_availability(prolog, game, platform):
    query = f"game_platform({game}, {platform})"
    return bool(list(prolog.query(query)))

def query_multiplatform_games(prolog):
    result = list(prolog.query("is_multiplatform(Game)"))
    return [r["Game"] for r in result]

def query_action_element_games(prolog):
    result = list(prolog.query("contains_action_elements(Game)"))
    return [r["Game"] for r in result]

def query_well_known_games(prolog):
    result = list(prolog.query("is_well_known_game(Game)"))
    return [r["Game"] for r in result]

def query_games_by_platform(prolog, platform):
    query = f"game_platform(Game, {platform})"
    result = list(prolog.query(query))
    return [r["Game"] for r in result]
