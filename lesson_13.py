class Answer:
    def __init__(self, question):
        from random import choice
        self.__rez = choice(['да', 'нет'])

    def __str__(self):
        return self.__rez

class Foreteller:
    def predict(self, question):
        answer = Answer(question)
        return answer

class Question:
    def __init__(self):
        self.__value__ = input('Что вы хотите узнать? ')

foreteller = Foreteller()
question = Question()
print(foreteller.predict(question))
