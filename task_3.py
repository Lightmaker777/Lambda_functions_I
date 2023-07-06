# Task 3
# lambda function assigned to a variable named starts_with_p that takes a single argument as a string. Returns True if this string starts with P (case insensitive) and False if it does not.

starts_with_p = lambda string: string.lower().startswith('p')

print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))
