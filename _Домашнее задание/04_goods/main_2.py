goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product, code in goods.items():
    in_total_quantity = 0
    in_total_price = 0
    for goods in store[code]:
        in_total_quantity += goods['quantity']
        in_total_price += goods['quantity'] * goods['price']
    print(f'{product} - {in_total_quantity} шт, стоимость: {in_total_price} руб.')
