numbers = list(range(1, 11))

# Squares of odd numbers
result = [n**2 for n in numbers if n % 2 != 0]

print(result)
