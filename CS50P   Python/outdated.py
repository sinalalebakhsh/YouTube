
dict_of_month = {
    "January"   :  1 ,
    "February"  :  2 ,
    "March"     :  3 ,
    "April"     :  4 ,
    "May"       :  5 ,
    "June"      :  6 ,
    "July"      :  7 ,
    "August"    :  8 ,
    "September" :  9 ,
    "October"   : 10 ,
    "November"  : 11 ,
    "December"  : 12 ,
}

while True:
    user_input = input('Date: ')
    if '/' in user_input:
        user_input1 = user_input.strip() # 1/50/2000
        new_input = user_input1.split('/') # ['1' , '50' , '1912']
        index0 = new_input[0]
        index1 = new_input[1]
        if index0 in dict_of_month.keys():
            continue
        if int(index1) > 31:
            continue
        if int(index0) < 13 :
            print(f'{new_input[2]}-{int(index0):02}-{int(index1):02}')
            break
    elif ',' in user_input:#['10' , 'December' , '1815' ]
        new_input = user_input.replace(',', '').split(' ')
        index1 = new_input[1]
        if index1 in dict_of_month.keys():
            continue
        if int(index1) > 31:
            continue
        if new_input[0] in dict_of_month.keys():
            print(f'{new_input[2]}-{dict_of_month[new_input[0]]:02}-{int(new_input[1]):02}')
            break
