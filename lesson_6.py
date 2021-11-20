from pprint import pprint


class User:
    """Простой класс пользователя"""

    def __init__(self, nickname, first_name, last_name, age, city, profession):
        self.first_name, self.last_name, self.age = first_name, last_name, age
        self.city, self.profession = city, profession
        self.nickname = nickname

    def __repr__(self):
        return "User('%s', '%s', '%s', '%s', '%s', '%s')" % (self.nickname, self.first_name,
                                                             self.last_name, self.age,
                                                             self.city, self.profession)


pasha = User('pasha', 'pavel', 'mayorov', 24, 'perm', 'engineer')
volodya = User('volodya', 'vladimir', 'putin', 69, 'moscow', 'president')
dima = User('dima', 'dmitriy', 'medvedev', 56, 'moscow', 'vicepresident')
users = {
    pasha.nickname: pasha,
    volodya.nickname: volodya,
    dima.nickname: dima,
}
pprint(users)
pprint(users[pasha.nickname])


def compare_2(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count / max(len(s1), len(s2))


def search_user_by_criteria():
    while True:
        print('To exit enter "q".')
        criteria = input('Enter your criteria for the user you want to find: ')
        if criteria == 'q':
            break
        elif criteria == 'age':
            meaning_start = int(input('Enter start of age range: '))
            meaning_finish = int(input('Enter finish of age range: '))
            for key in users:
                if meaning_start < users[key].age < meaning_finish:
                    print(key.title())
        elif criteria == 'first name':
            meaning = input('Enter the first name you want to find: ')
            for key in users:
                result = compare_2(users[key].first_name, meaning)
                if result > 0.6:
                    print(key.title())
        else:
            print('Your criteria is not correct')


search_user_by_criteria()
