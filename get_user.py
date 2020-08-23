import json

def get_user():
    """Get username if available."""
    user = input('What is your username? ')
    filename = f'{user}.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
