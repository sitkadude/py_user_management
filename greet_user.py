import json

from get_user import get_user
from create_user import create_user

def greet_user():
    """Greet the user."""
    username = get_user()
    if username:
        print(f'Welcome back, {username}.')
    else:
        print("We are not finding that username, let's create one.")
        username = create_user()
        print(f'Welcome to the vault, {username}.')
