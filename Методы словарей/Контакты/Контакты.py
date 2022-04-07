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
print(phonebook)

phonebook['Гоша'] = phonebook.pop('Игорь')
print(phonebook)

phonebook.pop('Гоша')
print(phonebook)

phonebook.update({'Гарик': 1500})
print(phonebook)

print(phonebook.get('Гарик'))  # 1500
print(phonebook.get('Гоша'))  # None
