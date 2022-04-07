n = int(input('Кол-во стран: '))
country_dict = dict()
ww = {}

for i in range(n):
    text = input(f'{i + 1} страна: ').split()
    for country in range(len(text[1:])):
        country_dict[text[0]] = [i_country for i_country in text[1:]]

print('country_dict', country_dict)
print()

for i in range(1, 4):
    city = input(f'{i} город: ')
    for q, x in country_dict.items():
        if city in x:
            print(f'Город {city} расположен в стране {q}')
            break

print(f'По городу {city} данных нет.')
