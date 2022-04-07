# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }

def structure():
    member = {'name': input('Введите имя: '),
              'surname': input('Введите фамилию: '),
              'hobbies': input('Перечислите хобби через запятую: ').split(','),
              'age': int(input('Введите возраст: ')),
              'children': list()
              }
    while True:
        children = input('Дети "да", "нет": ')
        if children.lower() == 'да':
            member['children'].append({'name': input('Имя ребенка: '), 'age': input('Сколько лет ребенку: ')})
        elif children.lower() == 'нет':
            break
    return member


family = structure()
print(family)

find_name_child = input('Введите имя ребенка: ')

for i in family['children']:
    if i.get('name') == find_name_child:
        print(f'найден {find_name_child} по фамилии', family['surname'])
        break
    else:
        print('Nosurname')
