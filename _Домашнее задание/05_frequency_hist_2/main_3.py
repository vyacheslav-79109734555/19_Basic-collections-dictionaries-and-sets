def record_letter(txt_set, txt):
    return {letter: txt.count(letter) for letter in txt_set}


def inverted_text(key, text_diCt):
    for i in key:
        inverted_text_dict.setdefault(i, [])
    for k, v in text_diCt.items():
        inverted_text_dict[v].append(k)


text = input('Введите текст: ')
text_set = sorted(set(text))
text_dict = record_letter(text_set, text)

print('Оригинальный словарь частот:')
for k, v in text_dict.items():
    print(f'{k} : {v}')

print('Инвертированный словарь частот:')
inverted_text_dict = dict()
counter = set()
for v in text_dict.values():
    counter.add(v)

inverted_text(counter, text_dict)
for i in inverted_text_dict:
    print(f'{i} : {inverted_text_dict[i]}')
