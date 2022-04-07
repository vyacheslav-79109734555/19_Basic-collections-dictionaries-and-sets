example = dict()
example['Ваня'] = 1000
print(example)  # {'Ваня': 1000}
example['Петя'] = 1000
print(example)  # {'Ваня': 1000, 'Петя': 1000}
example['Ваня'] = 5000
print(example)  # {'Ваня': 5000, 'Петя': 1000}
