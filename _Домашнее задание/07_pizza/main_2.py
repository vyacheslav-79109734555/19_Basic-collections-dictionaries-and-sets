def function_order(name_f, pizza_f, quantity_f):
    name_f[pizza_f] = name_f.setdefault(pizza_f, 0) + quantity_f
    return name_f


order_dict = dict()
for i in range(int(input('Введите кол-во заказов: '))):
    name, pizza, quantity = input(f'{i + 1} заказ: ').rsplit(' ', 3)
    order_dict[name] = (function_order(order_dict.get(name, {}), pizza, int(quantity)))
    print(order_dict)

for name in sorted(order_dict):
    print(name)
    for pizza, quantity in sorted(order_dict.get(name).items()):
        print(f'       {pizza} : {quantity}')
