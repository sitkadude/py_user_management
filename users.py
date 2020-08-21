class User:
    
    def __init__(self, first_name, last_name, login_attempts=0, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

        for key, value in kwargs.items():
            setattr(self, key, value)

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print(f'Welcome, {self.first_name.title()} {self.last_name.title()}.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

person_1 = User('lukas', 'jorgensen', warrior_type='viking', gender='male')
person_2 = User('soren', 'jorgensen', warrior_type='rogue', gender='male')
person_3 = User('carolyn', 'jorgensen', warrior_type='samurai', gender='female')

person_1.describe_user()
person_1.greet_user()
print('\n')

person_2.describe_user()
person_2.greet_user()
print('\n')

person_3.describe_user()
person_3.greet_user()
print('\n')

person_1.increment_login_attempts()
print(f'{person_1.login_attempts}')

person_1.reset_login_attempts()
print(f'{person_1.login_attempts}')

