punctuation_mark = set(".,;:!?")
txt = input('Введите строку: ')
count = [symbol for symbol in txt if symbol in punctuation_mark]
print(txt)
print(f'Количество знаков пунктуации: {len(count)}')
