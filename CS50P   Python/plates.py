import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(user_input):
    if user_input[:2].isalpha():
        if len(user_input) >= 2 and len(user_input) <= 6:  #lkjasdkljasd
            if ' ' in user_input:
                return False
            if '.' in user_input:
                return False
            number_in_user_input = re.findall(r'\d+', user_input)
            if number_in_user_input == []:   #si11
                return True
            elif number_in_user_input[0][0] != '0': #si11slksdf11   len طول  from 1 start  but
                                                    #               index from 0 start
                if len(number_in_user_input) == 1 and user_input[-1].isdigit() : 
                    return True
    else:
        return False


main()
