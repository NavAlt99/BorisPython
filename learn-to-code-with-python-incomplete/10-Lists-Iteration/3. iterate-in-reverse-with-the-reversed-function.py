the_simpsons = ["Homer", "Merge", "Bart", "Lisa", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters.")

# print(reversed(the_simpsons)) #It prints in a location in computer memory 
# print(type(reversed(the_simpsons))) # type list_reverseiterator different type of object called generator object
# behind the scene: generator objects store all the elements in memory, but just the next one. 



for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters.")
