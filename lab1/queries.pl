% Простые запросы для поиска фактов:

% Проверить, является ли Skyrim игрой жанра RPG
game_genre(skyrim, rpg).

% Найти все платформы, на которых доступна игра Skyrim
game_platform(skyrim, Platform).


% Запросы с логическими операторами:

% Найти все игры, которые либо шутеры, либо головоломки
game_genre(Game, shooter); game_genre(Game, puzzle).

% Проверить, что Skyrim не является головоломкой
\+ game_genre(skyrim, puzzle).


% Запросы с переменными:

% Найти все игры и их жанры
game_genre(Game, Genre).

% Найти все игры, которые можно играть на PC
game_platform(Game, pc).


% Запросы, требующие выполнения правил:

% Найти все мультиплатформенные игры
is_multiplatform(Game).

% Проверить, является ли игра Halo известной
is_well_known_game(halo).

% Найти все игры, доступные на PC
is_available_on_pc(Game).

% Проверить, является ли игра Mario игрой Nintendo
is_nintendo_adventure_game(mario).

% Найти все игры, которые содержат элементы действия
contains_action_elements(Game).
