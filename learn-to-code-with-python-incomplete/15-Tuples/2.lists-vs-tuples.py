birthday = (2, 5, 1988)

# print(len(birthday))

# print(birthday[0])
# print(birthday[1])
# print(birthday[2])
# print(birthday[15]) tuple index out of range

# print(birthday[-1])
# print(birthday[-2])
# print(birthday[-3])

# breakpoint[1] = 13  object does not support item assignment, tuples are immutable 

#** tuples can have mutable objects with in it 

address = (
    ['Hudson Street', 'New York', 'NY'],
    ['Franklin Street', 'San Francisco', 'CA']
)

address[1][0] = "Polk Street"

# print(address)

print(dir(birthday))