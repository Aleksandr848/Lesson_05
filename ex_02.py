# -- coding: utf-8 --  # Выдавало ошибку. Нашёл такое решение в интернете.
with open("bob.txt") as file:
    lines = file.readlines()
    number_of_lines = len([line for line in lines])
    print(f'Количество строк в файле - {number_of_lines}')
    i = 1
    for line in lines:
        number_of_words = len(line.split(' '))
        print(f'Количество слов в {i}-й строке - {number_of_words}')
        i += 1
