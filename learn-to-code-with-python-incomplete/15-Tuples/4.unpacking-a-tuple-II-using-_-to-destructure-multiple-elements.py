employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee

print(first_name)
print(last_name)
print(*details)
print(details)


*names, position, age = employee 
print()
print(*names)
print(position)
print(age)


first_name, *details, age = employee
print()
print(first_name)
print(*details)
print(age)


first_name, last_name, position, *details = employee
print()
print(first_name)
print(last_name)
print(position)
print(details)

