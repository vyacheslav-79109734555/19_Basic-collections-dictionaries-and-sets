data = dict()
# до этого что-то происходит

# print(data['server'])  # в print будет ошибка: // KeyError: 'server'

# TODO во время тестирования и что-бы избежать ошибки нужен метод: get()
print(data.get('server'))  # в print будет: None

data['server'] = {
    'host': '127.0.0.1',
    'port': '10'
}
# до этого что-то происходит

if data.get('configuration', {}).get('ssh', {}).get('login', {}):
    print('В структуре уже есть логин:')

data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}

print(data)
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин:')
