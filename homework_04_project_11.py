# Homework 04, Project 11: Printing of triangle by 'X'.

n = int(input('Put number of X: '))
if n > 0:
    for a in range(n):
        for b in range(0, a+1):
            print('X', end=' ')
        print(end='\n')
else:
    print('Put number greater than zero.')