#Write a recursive function to calculate sum of first N natural numbers.

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(f'The sum is: {sum(5)}')

#Write a recursive function to calculate sum of first N odd natural numbers
def sum_odd(n):
    if n==1:
        return 1
    return 2*n-1 + sum_odd(n-1)

print(f'The sum of odd numbers is: {sum_odd(5)}')

#Write a recursive function to calculate sum of first N even natural numbers.
def sum_even(n):
    if n==1:
        return 1
    return 2*n + sum_even(n-1)

print(f'The sum of even numbers is: {sum_even(5)}')

#Write a recursive function to calculate factorial of a number.
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(f'The factorial is: {fact(5)}')

#Write a recursive function to calculate sum of squares of first N natural numbers.
def squares(n):
    if n==1:
        return 1
    return n*n + squares(n-1)

print(f'The square is: {squares(5)}')