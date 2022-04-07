# TODO: Словарь - быстрый способ

phonebook_dict = {
    'Ваня': 88006663636,
    'Петя': 88006663535,
    'Лена': 88006663434
}

name = input('Введите имя: ')

if name in phonebook_dict:
    print('Телефон абонента: {0}'.format(name), phonebook_dict[name])
else:
    print('Ошибка: человек с именем {0} не найден.'.format(name))

