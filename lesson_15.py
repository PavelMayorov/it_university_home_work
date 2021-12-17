class MyInt(int):

    def __add__(self, x):
        return super().__add__(x+1)


y = MyInt(2)
print(y + 2)


class MyList(list):

    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('> 10')
        else:
            super().__init__(x)

    def append(self, x):
        if len(self) == 10:
            raise ValueError('> 10')
        else:
            super().append(x)


# y = MyList([1, 2, 3])
# for i in range(10):
#     y.append(i)
#     print(y, len(y))


class MyList2(set):
    pass


y = MyList2([1, 1, 2, 2, 3, 3])
print(y)
