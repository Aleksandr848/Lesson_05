import json
with open("data.txt") as file:
    firm = file.readlines()
    average_profit = 0
    sum_profit = 0
    dict_firm_profit = {}
    i = 0
    for lines in firm:
        line = list(lines.split())
        firm_profit = int(line[-2]) - int(line[-1])
        dict_firm_profit[line[0]] = firm_profit
        if firm_profit > 0:
            sum_profit += firm_profit
            i += 1
    average_profit = sum_profit / i
    dict_average_profit = {"average_profit": average_profit}
    list_firm = [dict_firm_profit, dict_average_profit]
with open("data.json", "w", encoding="utf-8") as write_f:
    json.dump(list_firm, write_f)
    # json_str = json.dumps(list_firm, sort_keys=False, indent=4, ensure_ascii=False)
    # print(json_str)
