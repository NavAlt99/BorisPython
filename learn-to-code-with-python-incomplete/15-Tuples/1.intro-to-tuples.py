# immutable lists 

food = "Sushi", "Steak", "Guacamole"
print(food)
food = ("Sushi", "Steak", "Guacamole")
print(food)

print(type(food))

empty = ()
print(type(empty))

# mystery = (1)
# print(type(mystery))

mystery = 1, 
print(type(mystery))

print(tuple(["Sushi", "Steak", "Guacomole"]))
print(type(tuple(["Sushi", "Steak", "Guacomole"])))

print(tuple(["abc"]))

numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)

all_numbers = (numbers_a, numbers_b, numbers_c)
print(all_numbers)