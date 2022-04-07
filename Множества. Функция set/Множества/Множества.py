num_1 = {1, 2, 3, 4, 5}
num_2 = {4, 5, 6, 7, 8}

print(num_1.intersection(num_2), 'метод.intersection() - обозначает пересечение множеств /num_1 и num_2/')

print(num_1 & num_2, '& - обозначает пересечение множеств /num_1 и num_2/')

print(num_1.union(num_2), 'метод.union() - обозначает объединение множеств /num_1 и num_2/')

print(num_1 | num_2, '| - обозначает объединение множеств /num_1 и num_2/')

print(num_1.difference(num_2), 'метод.difference() - обозначает разность множеств /num_1 и num_2/')

print(num_1 - num_2, '"-" - обозначает разность множеств /num_1 и num_2/')
