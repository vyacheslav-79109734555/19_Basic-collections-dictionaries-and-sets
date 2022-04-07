n = int(input('Введите кол-во заказов: '))
order_dict = dict()

for i in range(1, n + 1):
    record = input(f'{i} заказ: ')
    name, pizza, quantity = record.rsplit(maxsplit=3)  # имя, пицца, количество
    if name not in order_dict:
        order_dict[name] = {pizza: int(quantity)}
    else:
        if pizza not in order_dict:
            order_dict[name] |= {pizza: int(quantity)}
        else:
            order_dict[name][pizza] += int(quantity)

for name in sorted(order_dict):
    print(f'{name}:')
    for pizza, quantity in sorted(order_dict.get(name).items()):
        print(f'        {pizza} : {quantity}')
