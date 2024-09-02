# Rock Paper Scissors
import random


def main():
    list_items = ['r' , 'p' , 's']
    ai_choice_ = make_ai_choice(list_items)
    true_input = get_true_input(list_items)
    print(comparator_user_to_ai(true_input, ai_choice_))



def get_true_input(list_items):
    while True:
        user_input = input('Enter r p s: ')
        if user_input in list_items:
            true_input = user_input
            return true_input



def make_ai_choice(list_items):
    ai_choice = random.choice(list_items)
    return ai_choice


def comparator_user_to_ai(true_input, ai_choice_):
    if true_input == ai_choice_:
        return 'Equal'
    elif true_input == 'r' and ai_choice_ == 'p':
        return 'Computer won'
    elif true_input == 'p' and ai_choice_ == 's':
        return 'Computer won'
    elif true_input == 's' and ai_choice_ == 'r':
        return 'Computer won'
    else:
        return 'You won'


if __name__ == "__main__":
    main()
