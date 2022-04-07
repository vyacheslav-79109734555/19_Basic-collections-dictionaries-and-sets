violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83,
    '4': 2.2,
    '5': 3.3,
    '6': 4.4
}
total_time = 0
selection = int(input('Сколько песен выбрать? '))
compilation = set(input(f'Название {i + 1} песни: ') for i in range(selection))

for i in compilation:
    if i in violator_songs.keys():
        total_time += violator_songs[i]
    else:
        print('Такой песни нет')
print(f'\nОбщее время звучания песен: {round(total_time, 2)} минут')
