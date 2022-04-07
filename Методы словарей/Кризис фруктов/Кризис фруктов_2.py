def data(text):
    summ = sum(text.values())
    arr = list(text)[list(text.values()).index(min(text.values()))]
    print('Общий доход за год составил:', summ)
    print('Самый маленький доход у', arr, '. Он составляет ', min(text.values()), 'рублей')
    text.pop(arr)

    return text


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
dictionary = data(incomes)

print('Итоговый словарь: \n', dictionary)
