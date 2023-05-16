# List comprehensions allow us to create a new list with single line code. 
numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)
# print(number)

squares = [number ** 2 for number in numbers]
print(squares)


rivers = ["Amazon", "Nile", "Ganga", "Yangtze"]
print([len(river) for river in rivers])


expressions = ["lol", "rofl", "lmao"]
print([exp.upper() for exp in expressions])

decimals = [4.95, 3.14, 2.01]
print([int(decimal) for decimal in decimals])