import numpy as np
from random import randint

row = np.array(range(100))
summ = np.sum(row)
print(summ)

while True:
    print('')
    row_length = input('Enter row length or "q" to end the program: ')
    if row_length == 'q':
        break
    row = np.array(range(int(row_length)))
    summ = np.sum(row)
    print(f'Row sum = {summ}.')

row = np.array(range(randint(0, 100)))
summ = np.sum(row)
print(summ)
