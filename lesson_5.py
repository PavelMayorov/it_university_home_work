def search_oldest_user_in_list(test_list):
    age_all_users = test_list[2::5]
    result = sorted(age_all_users, reverse=True)[0]
    return result


def search_oldest_user_in_dict(test_dict):
    age_all_users = []
    for user in test_dict:
        age_all_users.append(test_dict[user]['age'])
    result = sorted(age_all_users, reverse=True)[0]
    return result


def compare(s1, s2):
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))


def compare_2(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count / max(len(s1), len(s2))


users_info_in_list = ['pavel', 'mayorov', '24', 'perm', 'engineer', 'vladimir', 'putin', '69', 'moscow', 'president',
                      'dmitriy', 'medvedev', '56', 'moscow', 'vicepresident']

users_info_in_dict = {'user_1': {'first_name': 'pavel',
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

print(search_oldest_user_in_list(users_info_in_list))
print(search_oldest_user_in_dict(users_info_in_dict))
print(compare('компьютер', 'компьютеризация'))
print(compare('лада', 'лалалэнд'))
print(compare_2('компьютер', 'компьютеризация'))
print(compare_2('лада', 'лалалэнд'))
