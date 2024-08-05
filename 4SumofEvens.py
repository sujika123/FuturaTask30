#4. Write a function sum_of_evens(n) that takes an integer n and returns the sum of all even numbers from 1 to n.

def sum_of_evens(n):
    sum =0
    for i in range(1,n+1,1):
        if(i%2 == 0):
            sum = sum + i
    return sum

n =int(input("Enter the value of n : "))
print(sum_of_evens(n))