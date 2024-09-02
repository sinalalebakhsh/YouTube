import random

user_input = 0 # =1
ai_choice = 0

while True:
    try:
        get_input = int(input('Level:')) # 1
        if get_input > 0:
            user_input = get_input
            ai_choice = random.randint(1,get_input) # 1   10
            break
    except ValueError:
        pass
    except EOFError:
        print('\r')
        break

while True:
    try:
        get_guess = int(input('Guess: ')) # 1 10
        if get_guess == ai_choice:
            print('Just right!')
            break
        elif get_guess > ai_choice:
            print('Too large!')
        elif get_guess < ai_choice:
            print('Too small!')
    except ValueError:
        pass
