import json

def create_user():
    """Prompt for new username."""
    while True:
        username = input('Enter your new username: ')
        confirm = input(f'Would you like to confirm {username} as your new username? (y/n) ')
        if confirm.lower() == 'y':
            filename = f'{username}.json'
            with open(filename, 'w') as f:
             json.dump(username, f)
            return username
        else:
            continue
