with open("text.txt", "w", encoding="utf-8") as file:
    flag = True
    while flag:
        line = input('Введите какую-нибудь дичь: ')
        if line == '':
            flag = False
        else:
            file.write(line + '\n')

