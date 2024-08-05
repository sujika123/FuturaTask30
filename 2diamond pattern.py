#Write a function  to print diamond pattern

n = 5
# Print the upper part of the diamond
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

 # Print the lower part of the diamond
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

