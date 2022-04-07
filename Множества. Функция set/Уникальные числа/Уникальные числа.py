import random

numb_list = [random.randint(1, 5) for _ in range(10)]  # генератор случайных чисел [3, 4, 2, 3, 4, 5, 1, 5, 1, 3]
arr = set(numb_list)  # set -- структура данных -- МНОЖЕСТВО

print(arr)  # {1, 2, 3, 4, 5}

# *************************************************************
# или
# *************************************************************

new_list = []
for i_numb in numb_list:
    if i_numb not in new_list:
        new_list.append(i_numb)
print(numb_list)  # [3, 4, 2, 3, 4, 5, 1, 5, 1, 3]
print(new_list)  # [3, 4, 2, 5, 1]
