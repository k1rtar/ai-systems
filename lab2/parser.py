import re
from knowledge_base import load_knowledge_base, is_valid_genre, is_valid_platform, is_valid_developer


PATTERN_MAP = {
    'genres': r'мне нравятся жанры (.+)',
    'developer': r'рекомендованные игры от разработчика (.+)',
    'platform': r'порекомендуй игры на платформе (.+)',
    'well_known_games': r'рекомендованные игры от известных разработчиков',
    'availability': r'есть ли игра (.+) на платформе (.+)',
    'multiplatform': r'какие игры являются мультиплатформенными',
    'action_elements': r'порекомендуй игры с элементами действия'
}

def parse_input(user_input: str):
    """
    Функция для парсинга строки ввода пользователя и валидации параметров.
    
    :param user_input: строка, введенная пользователем
    :return: кортеж (тип запроса, параметры)
    """
    user_input = user_input.casefold().strip()  
    prolog = load_knowledge_base()

    
    for query_type, pattern in PATTERN_MAP.items():
        match = re.search(pattern, user_input)
        if match:
            if query_type == 'genres':
                genres = match.group(1).split(', ')
                genres = [genre.strip().strip('.,!?') for genre in genres]  
                for genre in genres:
                    if not is_valid_genre(prolog, genre):
                        raise ValueError(f"Жанр '{genre}' не найден в базе знаний.")
                return query_type, genres
            elif query_type == 'developer':
                developer = match.group(1).strip().strip('.,!?')
                if not is_valid_developer(prolog, developer):
                    raise ValueError(f"Разработчик '{developer}' не найден в базе знаний.")
                return query_type, developer
            elif query_type == 'platform':
                platform = match.group(1).strip().strip('.,!?')
                if not is_valid_platform(prolog, platform):
                    raise ValueError(f"Платформа '{platform}' не найдена в базе знаний.")
                return query_type, platform
            elif query_type == 'availability':
                game = match.group(1).strip().strip('.,!?')
                platform = match.group(2).strip().strip('.,!?')
                if not is_valid_platform(prolog, platform):
                    raise ValueError(f"Платформа '{platform}' не найдена в базе знаний.")
                return query_type, (game, platform)
            elif query_type in ['multiplatform', 'action_elements', 'well_known_games']:
                return query_type, None

    
    raise ValueError("Некорректный формат ввода. Попробуйте снова.")
