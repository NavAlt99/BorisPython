salutation = "Mr. Rambabu the blob"

# startswith returns true if the substring is found at the begnning of the string.

print(salutation.startswith("Mr"))
print(salutation.startswith("mr"))
print(salutation.startswith("Ram"))
print(salutation.startswith("Mr. Ram"))
print(salutation.startswith("M"))
print(salutation.startswith("m"))

print()

print(salutation.endswith("ob"))
print(salutation.endswith("blob"))
print(salutation.endswith("Blob"))
print(salutation.endswith("b"))
print(salutation.endswith("bo"))