import re
with open("subject.txt") as file:
    subject = file.readlines()
    dict_sub = {}
    for lines in subject:
        line = list(re.sub("[^0123456789 ]","", lines).split())
        hours = sum([int(lin) for lin in line])
        key = "".join(el for el in list(lines.split()[0]) if el.isalpha())
        dict_sub[key] = hours
    print(dict_sub)
