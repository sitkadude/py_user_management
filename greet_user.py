import json

def greet_user():

    while True:
        user = input('Enter username: ')
        filename = f'{user}.json'
        
        try:
            with open(filename) as f:
                username = json.load(f)
        except FileNotFoundError:
            confirm = input('This username does not exist, would you like to create this username? (y/n) ')
            if confirm.lower() == 'y':
                with open(filename, 'w') as f:
                    json.dump(user, f)
                    print(f'{user} is your new username.')
                    break
            else:
                print('Please start over.\n')
                continue
        else:
            print(f'Welcome back, {user}.')
            break
