import random

n_max = int(input('Введите максимальное число: '))  # максимальное число
hidden_number = str(random.randint(1, n_max))  # str - скрытое число
num_plenty = {str(x) for x in range(1, n_max + 1)}  # str - множество

while True:
    num_lict = {num for num in input('Нужное число есть среди вот этих чисел: ').split()}
    print(num_lict)
    if num_lict == {'помогите'}:
        print(f'Загаданное число: {hidden_number}')
        break
    if len(num_lict) == 1 and num_lict == {str(hidden_number)}:
        print(f'Верно. Загаданное число: {hidden_number}')
        break
    print('Ответ Артёма: ', end='')
    if hidden_number in num_lict:
        print('Да')
        num_plenty = num_lict
    else:
        print('Нет')
        num_plenty.difference_update(num_lict)
