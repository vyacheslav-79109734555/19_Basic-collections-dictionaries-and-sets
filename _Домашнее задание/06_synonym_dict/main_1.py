def dictionary_of_words(word):
    if text_dict.get(word):
        print(f'Синоним: {text_dict.get(word).title()}')
        return True
    else:
        print(f'Слова: {word} в словаре нет.')
        return False


n = int(input('Введите количество пар слов: '))
text_dict = dict()
for i in range(1, n + 1):
    txt = input(f'{i} пара: ').lower().split(' - ')
    text_dict.update({txt[0]: txt[1]})
    text_dict.update({txt[1]: txt[0]})

while True:
    word_str = input('Введите слово: ').lower()
    if dictionary_of_words(word_str) is True:
        break
