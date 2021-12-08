from random import choice


def compare_2(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count / max(len(s1), len(s2))


def random_answer():
    answers = {}
    while True:
        print('To exit enter "q".')
        question = input('Enter your question: ')
        if question == 'q':
            break
        else:
            flag = True
            for key in answers:
                result = compare_2(key, question)
                if result > 0.6:
                    print(answers[question])
                    flag = False
            if flag:
                answer = choice(['yes', 'no'])
                print(answer)
                answers[question] = answer


random_answer()
