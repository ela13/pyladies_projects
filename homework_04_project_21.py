# Homework 04, Project 21: Division by 3, 5, and 3 and 5.

# n = float(input('Put figure: '))

for i in range(100):
    if (i % 3) == 0:
        print('Bum!')
    elif (i % 5) == 0:
        print('Bac!')
    elif (i % 3) == 0 and (i % 5) == 0:
        print('Bum-Bac!')
    else:
        print(i, 'is not divisible by 3, 5, or 3 and 5.')

