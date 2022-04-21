phonebook = {
    'Ваня': 100,
    'Петя': 200,
    'Алиса': 300
}
other_phonebook = {
    'Алена': 2000,
    'Петя': 800,
    'Игорь': 1000
}

phonebook.update(other_phonebook)
print('Объединение словарей:\n', phonebook)
print()

phonebook['Гоша'] = phonebook.pop('Игорь')
print('Замена ключа: Гоша на Игорь\n', phonebook)
print()

phonebook.pop('Гоша')
print('pop(Гоша) - Удалил ключ и значение Гоша:\n', phonebook)
print()

phonebook.update({'Гарик': 1500})
print('update({Гарик: 1500}) - Добавил ключ и значение Гарик:\n', phonebook)
print()

print('get(Гарик)) - показывает значение ключа Гарик =', phonebook.get('Гарик'))  # 1500
print(phonebook.get('Гоша'))  # None
