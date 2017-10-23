# Homework 04, Project 13: Printing of square by 'X'.

n = int(input('Put number of X: '))
if n > 0:
    for a in range(n):
        if a == 0 or a == (n-1):
            print(('X' + ' ')*(n-1) + 'X')
        else:
            print('X' + ' '*(2*n-3) + 'X')
else:
    print('Put number greater than zero.')