# -- coding: utf-8 --  # Выдавало ошибку. Нашёл такое решение в интернете.
with open("english.txt") as file:
    lines = file.readlines()
    numbers = ['Один', 'Два', 'Три', 'Четыре']
    with open("russian.txt", 'w') as rus_file:
        i = 0
        for line in lines:
            st = line.split()
            rus_file.write(numbers[i] + ' — ' + st[-1] + '\n')
            i += 1
