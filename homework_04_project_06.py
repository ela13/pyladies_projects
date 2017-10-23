# Homework 04, Project 06: Printing of row order.

n = int(input('Put number of rows: '))
if n > 0:
    for rowNumber in range(n):
        print('Row', rowNumber)
else:
    print('Put number greater than zero.')