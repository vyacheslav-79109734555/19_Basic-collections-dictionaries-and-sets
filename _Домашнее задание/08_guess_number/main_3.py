# хороший вариант
import random

n_max = int(input('Введите максимальное число: '))
n_secret = {(random.randint(1, n_max))}
n_set = set(range(1, n_max + 1))
print(n_set)

while True:
    n_lict = input('Загаданное число есть среди вот этих чисел: ')
    if 'помогите' in n_lict:
        print(f'Загаданное число: {n_secret}')
        break

    else:
        numb = set(list(map(int, n_lict.split())))
        if len(numb) == 1 and numb == n_secret:
            print(f'Верно. Загаданное число: {n_secret}')
            break

        if n_secret.intersection(numb):
            print('Ответ Артёма: Да')
            n_set = numb
        else:
            n_set.difference_update(numb)
            print(f'Ответ Артёма: НЕТ , но оно где то здесь: {n_set} ')
