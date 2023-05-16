def product(a, b):
    return a * b

# print(product(4, 5))

numbers = [3, 5]

numbers = (4, 5)

# print(product(numbers)) #TypeError: product() missing 1 required positional argument: 'b'

print(product(*numbers))
