n_max = int(input('Введите максимальное число: '))
num_plenty = set(range(1, n_max + 1))  # множество
print(num_plenty)

while True:
    num_lict = input('Нужное число есть среди вот этих чисел: ')
    if num_lict == 'помогите':
        break
    else:
        numb = set(list(map(int, num_lict.split())))
        txt = input('Ответ Артёма: ')
        if txt == 'да':
            num_plenty = num_plenty.intersection(numb)
        else:
            num_plenty = num_plenty.difference(numb)

num_plenty = sorted(num_plenty)
print('Артём мог загадать следующие числа:', *num_plenty)
