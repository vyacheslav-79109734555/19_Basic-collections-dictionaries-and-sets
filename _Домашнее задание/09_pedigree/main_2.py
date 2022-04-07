book_man = dict()

for i in range(int(input('Введите количество человек: ')) - 1):
    name_baby, name_parent = map(str, input(f'{i + 1} пара: ').split())
    book_man.update({name_baby: name_parent})

all_people_set = set(book_man.keys() | book_man.values())

family_tree = {}


def status(man):
    if man not in book_man:
        family_tree[man] = 0
        return 0
    parents_name = book_man[man]
    if name_parent in family_tree:
        count = family_tree[name_parent] + 1
    else:
        count = status(parents_name) + 1
    family_tree[man] = count
    return count


for people in all_people_set:
    family_tree[people] = status(people)

print('\n“Высота” каждого члена семьи:')
for i in sorted(family_tree):
    print(f'{i} : {family_tree[i]}')
