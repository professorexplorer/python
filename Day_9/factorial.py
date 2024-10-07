# Q2. Write a program to find the factorial of a given number.


def factotial(n):
    if n== 0 or n ==1:
        return 1
    else :
        return n * factotial(n-1)
    


factor= factotial(6)

print(factor)