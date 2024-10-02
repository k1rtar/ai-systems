
from parser import parse_input
from recommender import generate_recommendations
from constants import WELCOME_MESSAGE, HELP_MESSAGE, INPUT_ERROR_MESSAGE, EXIT_MESSAGE, INTERRUPT_MESSAGE, EOF_ERROR_MESSAGE, INPUT_PROMPT

def show_help():
    print(HELP_MESSAGE)

def main():
    print(WELCOME_MESSAGE)
    
    show_help()  

    while True:
        try:
            user_input = input(INPUT_PROMPT)
            
            if user_input.lower() == 'выход':
                print(EXIT_MESSAGE)
                break
            
            request_type, parameters = parse_input(user_input)
            recommendations = generate_recommendations(request_type, parameters)
            
            if recommendations:
                print(f"Рекомендации: {', '.join(recommendations)}")
            else:
                print("К сожалению, ничего не найдено по вашему запросу.")
        
        except ValueError:
            print(INPUT_ERROR_MESSAGE)
        except KeyboardInterrupt:
            print(INTERRUPT_MESSAGE)
            break
        except EOFError:
            print(EOF_ERROR_MESSAGE)
            break

if __name__ == "__main__":
    main()
