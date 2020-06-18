"""
    This program computes the factorial calculates
    of a factorial number.
"""

def print_factorial(n):

    if n == 1:

        return n
    else:
        print(str(n) + ' * ' + str(n-1) + ' = ' + str(n*n-1))
        return n * print_factorial(n-1)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print('factorial 8!')
print(factorial(8))


print(print_factorial(8))
