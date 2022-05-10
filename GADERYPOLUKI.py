while True:

    key = str(input('Wpisz klucz bez spacji i wielkimi literami:'))


    #Part of creating a code
    code = {}
    key_list = list(key)

    if len(key_list)%2 != 0:
        print('Błędny klucz!')
        exit()

    for length in range(0,len(key_list),2):
        code[f"{key_list[length]}"] = f'{key_list[(length)+1]}'
        code[f"{key_list[(length)+1]}"] = f'{key_list[length]}'

    #Part of creating code
    crypted = str(input('Podaj zaszyfrowaną wiadomość bez spacji i wielkimi literami:'))
    first = crypted

    #Ready code for example
    #first = 'YMTLJOLGU'

    is_correct = False

    #Part of decryption of the code
    while is_correct != True:
        user_code = str(input('Wpisz tutaj swoje hasło bez spacji i wielkimi literami:'))
        list_of_code = list(user_code)

        password = ''
        for letter in user_code:
            if letter in code:
                password = password + str(code[str(letter)])
            else:
                password = password + str(letter)
        if password == first:
            print('Gratulacje! Odgałeś kod!')
            is_correct = True
        else:
            print('Niestety, błędne hasło.')

    continue