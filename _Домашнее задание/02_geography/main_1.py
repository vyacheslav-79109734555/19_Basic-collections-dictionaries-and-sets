n = int(input('Кол-во стран: '))
country_dict = dict()

for i in range(n):
    country_dict[i] = input(f'{i + 1} страна: ').split()

for x in range(1, 4):
    flag = False
    city = input(f'{x} город: ')
    for i in country_dict:
        if city in country_dict[i]:
            print(f'Город {city} расположен в стране {country_dict[i][0]}')
            flag = True
    if not flag:
        print(f'По городу {city} данных нет.')
