# #Write a recursive function to print first N natural numbers.
# def f(n):
#     if n > 0:
#         f(n-1)
#         print(n, end = ' ')
# f(10)

# #Write a recursive function to print first N natural numbers in reverse order.
# def f_rev(n):
#     if n>0:
#         print(n, end = ' ')
#         f(n-1)

# f_rev(10)

#Write a recursive function to print first N odd natural numbers.
def f_evenreverse(n):
    if n>0:
        print(2*n, end=' ')
        f_evenreverse(n-1)
f_evenreverse(10)