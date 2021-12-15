class User:
    """Простая модель пользователя"""

    def __init__(self, first_name, last_name, age, city, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        print(f'User {self.first_name} {self.last_name} from {self.city} have {self.age} years.')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


pasha = User('pavel', 'mayorov', 24, 'perm', 'engineer')
volodya = User('vladimir', 'putin', 69, 'moscow', 'president')
dima = User('dmitriy', 'medvedev', 56, 'moscow', 'vicepresident')

pasha.greet_user()
volodya.describe_user()
dima.increment_login_attempts()
print(dima.login_attempts)
