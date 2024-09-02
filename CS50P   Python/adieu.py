import inflect

p = inflect.engine()

get_list_from_user = []
while True:
    try:
        get_input = input('Name: ')
        get_list_from_user.append(get_input)
    except EOFError:
        break

mylist = p.join(get_list_from_user)
print('Adieu, adieu, to', mylist)
