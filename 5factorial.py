#5. Write a function factorial(n) that calculates the factorial of a given number n using a for loop.

def factorial(n):
    f = 1
    for i in range(1, n + 1, 1):
        f = f * i
    return f

n = int(input("Enter the value of n : "))
print("Factorial of", n, "is",factorial(n))




