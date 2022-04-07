def record_letters(txt_set, txt):
    return {letter: txt.count(letter) for letter in txt_set}


text = input('Введите текст: ')
text_set = sorted(set(text))
text_dict = record_letters(text_set, text)

print('Оригинальный словарь частот:')
for k, v in text_dict.items():
    print(f'{k} : {v}')

print('\nИнвертированный словарь частот:')
inverted_text_dict = dict()
for k, v in text_dict.items():
    inverted_text_dict.setdefault(v, []).append(k)

for i in sorted(inverted_text_dict):
    print(f'{i} : {inverted_text_dict[i]}')

