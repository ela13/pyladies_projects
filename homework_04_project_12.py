# Homework 04, Project 12: Printing of rows.

n = int(input('Put number of rows: '))
if n > 0:
    for a in range(n):
        if a == 0:
            print('1st row')
        else:
            print('this is not 1st row')
else:
    print('Put number greater than zero.')

