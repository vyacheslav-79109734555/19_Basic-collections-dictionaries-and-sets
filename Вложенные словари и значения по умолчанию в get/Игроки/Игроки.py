players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
print('Все члены команды из команды А, которые отдыхают.')
members_team_A = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
print(members_team_A)

print('Все члены команды из группы B, которые тренируются.')
members_team_B = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
print(members_team_B)

print('Все члены команды из команды C, которые путешествуют.')
members_team_C = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
print(members_team_C)