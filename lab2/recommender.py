
from knowledge_base import (
    load_knowledge_base,
    query_games_by_genres,
    query_games_by_developer,
    query_game_availability,
    query_multiplatform_games,
    query_action_element_games,
    query_well_known_games,
    query_games_by_platform
)

def handle_genres(prolog, parameters):
    return query_games_by_genres(prolog, parameters)

def handle_developer(prolog, parameters):
    return query_games_by_developer(prolog, parameters)

def handle_platform(prolog, parameters):
    return query_games_by_platform(prolog, parameters)

def handle_availability(prolog, parameters):
    game, platform = parameters
    is_available = query_game_availability(prolog, game, platform)
    return [game] if is_available else []

def handle_multiplatform(prolog, parameters):
    return query_multiplatform_games(prolog)

def handle_action_elements(prolog, parameters):
    return query_action_element_games(prolog)

def handle_well_known_games(prolog, parameters):
    return query_well_known_games(prolog)

ACTION_MAP = {
    'genres': handle_genres,
    'developer': handle_developer,
    'platform': handle_platform,
    'availability': handle_availability,
    'multiplatform': handle_multiplatform,
    'action_elements': handle_action_elements,
    'well_known_games': handle_well_known_games,
}

def generate_recommendations(request_type, parameters):
    """
    Генерирует рекомендации на основе типа запроса и параметров.
    
    :param request_type: тип запроса
    :param parameters: параметры запроса
    :return: список рекомендаций
    """
    prolog = load_knowledge_base()
    
    action = ACTION_MAP.get(request_type)
    
    if action:
        return action(prolog, parameters)
    else:
        return []
