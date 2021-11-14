users_info_in_str = ['pavel', 'mayorov', 24, 'perm', 'engineer', 'vladimir', 'putin', 69, 'moscow', 'president',
                     'dmitriy', 'medvedev', 56, 'moscow', 'vicepresident']

users_info_in_tuple = {'user_1': {'first_name': 'pavel',
                                  'last_name': 'mayorov',
                                  'age': 24,
                                  'city': 'perm',
                                  'profession': 'engineer',
                                  },
                       'user_2': {'first_name': 'vladimir',
                                  'last_name': 'putin',
                                  'age': 69,
                                  'city': 'moscow',
                                  'profession': 'president',
                                  },
                       'user_3': {'first_name': 'dmitriy',
                                  'last_name': 'medvedev',
                                  'age': 56,
                                  'city': 'moscow',
                                  'profession': 'president',
                                  },
                       }

# Поиск самого старшего пользователя
age_all_users = users_info_in_str[2::5]
print(sorted(age_all_users, reverse=True)[0])

age_all_users = []
for user in users_info_in_tuple:
    age_all_users.append(users_info_in_tuple[user]['age'])
print(sorted(age_all_users, reverse=True)[0])

print('Enter new user data.')
while True:
    print('To exit enter "q".')
    nickname = input('Enter your nickname: ')
    if nickname == 'q':
        break
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age: ')
    city = input('Enter your city: ')
    profession = input('Enter your profession: ')
    users_info_in_tuple[nickname] = {}
    users_info_in_tuple[nickname]['first_name'] = first_name
    users_info_in_tuple[nickname]['last_name'] = last_name
    users_info_in_tuple[nickname]['age'] = age
    users_info_in_tuple[nickname]['city'] = city
    users_info_in_tuple[nickname]['profession'] = profession
    print(f'User {nickname} added.')

print(users_info_in_tuple)
