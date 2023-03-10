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