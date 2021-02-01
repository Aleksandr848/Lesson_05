# -- coding: utf-8 --  # Выдавало ошибку. Нашёл такое решение в интернете.
with open("salary.txt") as file:
    lines = file.readlines()
    losers = []
    sum = 0
    for line in lines:
        men = line.split()
        sum += float(men[-1])
        if int(men[1]) < 20000:
            losers.append(men[0])
    print('Зарплата меньше 20 тыс. - ' + ','.join(map(str, losers)))
    print(f'Средняя зарплата - {round(sum / len(lines), 2)}')
