# TODO : НЕ эффективный код

phonebook_list = [
    ['Ваня', 88006663636],
    ['Петя', 88006663535],
    ['Лена', 88006663434]
]
name = input('Введите имя: ')

is_exist = False
for i_person in phonebook_list:
    if i_person[0] == name:
        is_exist = True
        print('Телефон абонента: {0}'.format(name), i_person[1])
        break
if not is_exist:
    print('Ошибка: человек с именем {0} не найден.'.format(name))
