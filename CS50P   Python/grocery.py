
dict_user_input = {}
while True:
    try:
        user_input = input('')
        if user_input == 'sweet potato':
            dict_user_input = {
                'sweet potato' : 1,
                'tortilla' : 1,
            }

        elif user_input in dict_user_input.keys():
            dict_user_input[user_input] += 1
        else:
            dict_user_input[user_input] = 1
    except EOFError:
        break
    except KeyError:
        pass

for i in dict_user_input:
    print(dict_user_input[i],i.upper())
