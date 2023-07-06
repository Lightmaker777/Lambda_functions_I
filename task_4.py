# Task 4
# For a given list of numbers, use a lambda function to return the result of multiplying each number by a given number stored in a variable named factor in the global scope.

numbers = [2, 4, 5, 7, 9, 14]
factor = 2

result = list(map(lambda num: num * factor, numbers))
print(result)



