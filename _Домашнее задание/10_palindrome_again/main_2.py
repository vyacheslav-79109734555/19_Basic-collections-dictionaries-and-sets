def palindrome(txt):
    count_letter = 0
    for symbol in txt:
        if txt.count(symbol) % 2 != 0:
            count_letter += 1
    if count_letter > 1:
        return 'Нельзя сделать палиндромом'
    return 'Можно сделать палиндромом'


txt_str = input('Введите строку: ')
print(palindrome(txt_str))
