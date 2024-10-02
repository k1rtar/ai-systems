% Жанры видеоигр
genre(shooter).          
genre(rpg).              
genre(strategy).         
genre(puzzle).          
genre(adventure).       

% Платформы
platform(pc).            
platform(playstation).  
platform(xbox).          
platform(nintendo_switch). 
platform(mobile).        

% Разработчики
developer(nintendo).     
developer(bethesda).     
developer(ubisoft).      
developer(rockstar).     
developer(valve).
developer(bungie).
developer(firaxis).         

% Игры
game(mario).             
game(skyrim).            
game(halo).             
game(civilization).     
game(portal).            

% Игры и их жанры
game_genre(mario, adventure).   
game_genre(skyrim, rpg).        
game_genre(halo, shooter).      
game_genre(civilization, strategy). 
game_genre(portal, puzzle).     

% Игры и их платформы
game_platform(mario, nintendo_switch). 
game_platform(skyrim, pc).          
game_platform(skyrim, playstation). 
game_platform(halo, xbox).          
game_platform(portal, pc).          

% Игры и их разработчики
game_developer(mario, nintendo).    
game_developer(skyrim, bethesda).   
game_developer(halo, bungie).       
game_developer(civilization, firaxis). 
game_developer(portal, valve).      

% Правило: Игра является мультиплатформенной, если она доступна более чем на одной платформе
is_multiplatform(Game) :-              
    game_platform(Game, Platform1),
    game_platform(Game, Platform2),
    Platform1 \= Platform2.

% Правило: Игра является известной, если ее разработчик - Nintendo или Bethesda
is_well_known_game(Game) :-                
    game_developer(Game, nintendo);
    game_developer(Game, bethesda).

% Правило: Игра доступна на платформе PC
is_available_on_pc(Game) :-               
    game_platform(Game, pc).

% Правило: Игра является игрой Nintendo, если она в жанре приключений и доступна на Nintendo Switch
is_nintendo_adventure_game(Game) :-              
    game_genre(Game, adventure),
    game_platform(Game, nintendo_switch).

% Правило: Игра потенциально содержит элементы действия, если она является шутером
contains_action_elements(Game) :-        
    game_genre(Game, shooter).

