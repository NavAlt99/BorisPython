units = ["meter", "kilogram", "second", "amper", "kelvin", "candela", "mole", "Hertz"]

more_units = units.copy() 

# print(units)
# print(more_units)

units.remove("kelvin")
print(units)
print(more_units)


even_more_units = units[:] 
print(even_more_units)
