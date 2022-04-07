def palindrome(txt):
    str_dick = {}
    for i_sym in txt:
        str_dick[i_sym] = str_dick.get(i_sym, 0) + 1

    odd_count = 0
    for i_value in str_dick.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


txt_str = input('Введите строку: ')
if palindrome(txt_str):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
