import random


def get_level():
    levels = 0
    while levels not in [1,2,3]:
        try:
            levels = int(input('Level: '))
        except ValueError:
            pass
    return levels


def generate_integer(level):
    score = 0
    for i in range(10): # 0 9 = 10 دور حلقه
        if level == 1:
            num1 = random.randint(0,10)
            num2 = random.randint(0,10)
            num3 = num1 + num2
            try:
                user_input = int(input(f'{num1} + {num2} = '))
                if user_input == num3:
                    score += 1
                else:
                    print('EEE')
                    for i in range(2): # 0 , 1
                        user_input = int(input(f'{num1} + {num2} = '))
                        if user_input == num3:
                            score += 1
                        print('EEE')
                        if i == 1:
                            print(f'{num1} + {num2} = {num3}')
            except ValueError:
                ...
        if level == 2:
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            num3 = num1 + num2
            try:
                user_input = int(input(f'{num1} + {num2} = '))
                if user_input == num3:
                    score += 1
                else:
                    print('EEE')
                    for i in range(2):
                        user_input = int(input(f'{num1} + {num2} = '))
                        if user_input == num3:
                            score += 1
                        print('EEE')
                        if i == 1:
                            print(f'{num1} + {num2} = {num3}')
            except ValueError:
                ...
        if level == 3:
            num1 = random.randint(100,999)
            num2 = random.randint(100,999)
            num3 = num1 + num2
            try:
                user_input = int(input(f'{num1} + {num2} = '))
                if user_input == num3:
                    score += 1
                else:
                    print('EEE')
                    for i in range(2):
                        user_input = int(input(f'{num1} + {num2} = '))
                        if user_input == num3:
                            score += 1
                        print('EEE')
                        if i == 1:
                            print(f'{num1} + {num2} = {num3}')
            except ValueError:
                ...
    return score

def main():
    print(f'Score: {generate_integer(get_level())}')


if __name__ == "__main__":
    main()
