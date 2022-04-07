def function_order(record_f, order_dict_f):
    name, pizza, quantity = record_f[0], record_f[1], int(record_f[2])
    if name in order_dict_f:
        if pizza in order_dict_f[name].keys():
            order_dict_f[name][pizza] += quantity
        else:
            order_dict_f[name].update({pizza: quantity})
    else:
        order_dict_f.update({name: {pizza: quantity}})


order_dict = dict()
n = int(input('Введите кол-во заказов: '))

for i in range(1, n + 1):
    record = input(f'{i} заказ: ').split()
    function_order(record, order_dict)

print(order_dict)
for name in sorted(order_dict):
    print(name)
    for pizza in sorted(order_dict[name]):
        print(f'       {pizza} : {order_dict[name][pizza]}')
