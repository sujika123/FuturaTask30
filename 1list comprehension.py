# Write a list comprehension that returns a list of the squares of all even numbers between 1 and 20.

#Method 1

even_squares = [x**2 for x in range(2, 21, 2)]
print(even_squares)


#Method 2

squares_of_evens = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_of_evens)