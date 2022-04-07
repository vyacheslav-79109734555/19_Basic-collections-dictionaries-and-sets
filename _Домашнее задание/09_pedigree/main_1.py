def status(arr):
    if arr in book_man:
        return 1 + status(book_man[arr])
    else:
        return 0


book_man = {}

for i in range(int(input('Введите количество человек: ')) - 1):
    name_baby, name_parent = map(str, input(f'{i + 1} пара: ').split())
    book_man[name_baby] = name_parent

family_tree = {}

all_people = set(book_man.keys() | book_man.values())

for man in sorted(all_people):
    family_tree[man] = status(man)

print('\n“Высота” каждого члена семьи:')
for i in family_tree:
    print(f'{i} : {family_tree[i]}')
