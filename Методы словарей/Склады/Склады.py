small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
print(big_storage)

t = None
products = input('Введите название товара: ')
if big_storage.get(products) == t:
    print('товар:', products, 'отсутствует на складе:')
else:
    print('товар:', products, 'на складе:', big_storage[products])
