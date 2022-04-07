def histogram(txt):
    sym_dict = dict()
    for sym in txt:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input('Введите текст: ')
hist = histogram(text)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(f'{i_sym} : {hist[i_sym]}')

print('\nИнвертированный словарь частот:')

inverted_text_dict = dict()
for i_key, i_values in hist.items():
    inverted_text_dict.setdefault(i_values, []).append(i_key)

for i in inverted_text_dict:
    print(f'{i} : {inverted_text_dict[i]}')
