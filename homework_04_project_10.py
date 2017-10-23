# Homework 04, Project 10: Multiplication table.

n = int(input('Put figure: '))
if n > 0:
    for a in range(n):
        for b in range(n):
            print(a*b, end=' ')
        print(end='\n')
else:
    print('Put figure greater than zero.')