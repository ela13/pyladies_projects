# Homework 04, Project 09: Printing of square field by 'X'.

n = int(input('Put number of X: '))
if n > 0:
    for a in range(n):
        for b in range(n):
            print('X', end=' ')
        print(end='\n')
else:
    print('Put number greater than zero.')