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


def goods_list(good):
    return sum(i['quantity'] for i in store[good])


def price_list(good):
    return sum(i['quantity'] * i['price'] for i in store[good])


for production in goods:
    print(f'{production} - {goods_list(goods[production])}, стоимость: {price_list(goods[production])} руб.')
