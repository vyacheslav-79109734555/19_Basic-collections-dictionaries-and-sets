incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print('Общий доход за год составил:', sum(incomes.values()))

arr = list(incomes)[list(incomes.values()).index(min(incomes.values()))]

print('Самый маленький доход у', arr, '. Он составляет ', min(incomes.values()))

incomes.pop(arr)

print('Итоговый словарь:\n', incomes)
