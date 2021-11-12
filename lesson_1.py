string = 'ijhxljxxxjlk j  nmlkxxxx'
new_string = ''
for i in string:
    if i == 'x':
        i = 'y'
    new_string += i
print(new_string)

summ = 1
for i in range(1, 100):
    if (i % 3 == 0) or (i % 5 == 0):
        summ *= i
print(summ)

string = 'ijhxljxxxjlk j  nmlkxxxx'
print(string.replace('x', 'y'))
