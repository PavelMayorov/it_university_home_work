from random import choice


def compare(s1, s2):
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))


def checking_every_word(s1, s2, max_len):
    max_similarity_list = []
    for s1_word in s1.split():
        similarity_list = []
        for s2_word in s2.split():
            similarity_list.append(compare(s1_word, s2_word))
        max_similarity_list.append(max(similarity_list))
    return sum(max_similarity_list) / max_len


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
                max_len = max(len(key.split()), len(question.split()))
                similarity = checking_every_word(key, question, max_len)
                if similarity > (1 - (1 / max_len)):
                    print(answers[key])
                    flag = False
            if flag:
                answer = choice(['yes', 'no'])
                print(answer)
                answers[question] = answer


random_answer()
