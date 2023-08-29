# By Gonzalo Delgado




try:
    import random
    import os
    import pyttsx3
    from colors import *
except ModuleNotFoundError:
    with open('requirements.txt', 'w') as file:
        file.write('pyttsx3==2.90')
    print(f'{Color.RED}Failed to import required modules.{Color.RESET}')
    print(f'run this file {Color.YELLOW}"requirements.txt"{Color.RESET} as pip install -r requirements.txt')
    quit()

# Creando un motor de voz, para cantar el numero del bingo.
def sing(numero):
    engine = pyttsx3.Engine()
    engine.say(f'The number is {numero}')
    engine.runAndWait()

# Verifica el nombre del entorno, y ejecuta un comando para limpiar la pantalla.
def clean_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Creando el algoritmo para el sistema de distribucion de numeros de bingo.
def bingo():
    clean_screen()
    numeros = list(range(1, 91))
    repeating_numbers = []
    audio = False

    random.shuffle(numeros)
    
    
    try:
        text_or_audio = input(f'{Color.BLUE}[+]{Color.RESET} Would you like to receive the number by text or audio? (t/A) -> ').lower()
        if text_or_audio not in ['t', 'a']:
            print(f'{Color.RED}Invalid value{Color.RESET}, please choose between (t/A)')
            quit()
    except KeyboardInterrupt:
        print('\nExit successful!')
        quit()



    if text_or_audio == 't':
        audio = False
    elif text_or_audio == 'a':
        audio = True

    try:
        user_choice = input(f'{Color.BLUE}[+]{Color.RESET} Press "Enter" for get a number -> ')
       
    except KeyboardInterrupt:
        print('\nExit successful!')
        quit()

    while numeros:
        numero = numeros.pop()
        repeating_numbers.append(numero)
        if audio == True:
            sing(numero)
        else:
            print(f'\n{Color.RED}Random number{Color.RESET} {Color.BLUE}->{Color.RESET} {Color.YELLOW}{numero}{Color.RESET}\n')

        if not numeros:
            print(f'{Color.BLUE}[+]{Color.RESET} All the numbers have been pulled.')
        else:
            try:
                user_choice = input(f'{Color.BLUE}[+]{Color.RESET} Press "Enter" for get a number or "c" to check numbers -> ')

                if user_choice == 'c':
                    try:
                        boxes_length = int(input(f'{Color.BLUE}[+]{Color.RESET} Enter number of boxes -> '))
                    except ValueError:
                        print('You must enter an int value')
                    for index in range(boxes_length):
                        try:
                            number_verify = int(input(f'{Color.BLUE}[+]{Color.RESET} Enter the number to verify -> '))
                        except ValueError:
                            print('You must enter an int value')
                        if number_verify in repeating_numbers:
                            print('Yes!')
                        else:
                            print('No')
                    
            except KeyboardInterrupt:
                print('\nExit successful!')
                quit()


if __name__ == '__main__':
    try:
        bingo()
    except Exception as e:
        print(f'{Color.RED}Error: {e}{Color.RESET}')
else:
    print(f'{Color.BLUE}[+]{Color.RESET} You are an external file.')
