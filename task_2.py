# Task 2
# The functions isOdd, isEven and getParity from previous exercises, but now as lambda functions assigned to variables.

isOdd = lambda num: num % 2 != 0
isEven = lambda num: num % 2 == 0
getParity = lambda number, parity: (lambda num: num % 2 != 0)(number) if parity == 'odd' else (lambda num: num % 2 == 0)(number)

print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))
