# -- coding: utf-8 --  # Выдавало ошибку. Нашёл такое решение в интернете.
with open("numbers.txt", "w+") as file:
    numbers = input('Введите числа через пробел ').split()
    file.write(' '.join(map(str, numbers)))
with open("numbers.txt", "r") as file1:
    line = list(file1.read().split())
    sum_of_numbers = sum([int(lin) for lin in line])
    print(sum_of_numbers)
