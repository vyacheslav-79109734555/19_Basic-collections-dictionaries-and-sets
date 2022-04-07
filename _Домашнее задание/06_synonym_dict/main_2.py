n = int(input('Введите количество пар слов: '))
text_dict = dict()

for i in range(1, n + 1):
    txt = input(f'{i} пара: ').lower().split(' - ')
    text_dict.update({txt[0]: txt[1]})
    text_dict.update({txt[1]: txt[0]})

while True:
    word_str = input('Введите слово: ').lower()
    if text_dict.get(word_str):
        print(f'Синоним: {text_dict.get(word_str).title()}')
        break
    else:
        print(f'Слова: {word_str} в словаре нет.')
