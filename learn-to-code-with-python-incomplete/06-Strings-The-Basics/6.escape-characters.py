
print("\n\"\\n\" for newline ")
print("This will \nbegin a \nnewline") #\n for nextline 

print("\n\"\\t\" for tab")

print("Once upon a\ttime") #\t for tap

print("\n\"\\\""" for escape charecter")
print("\"To be or not to be\", said Hamlet") # \ infront of a charecter will make the charecter ignored
print("\'To be or not to be\', said Hamlet") # \ infront of a charecter will make the charecter ignored
print("Let's print a backslash: \\")


print("\nRaw Strings")

#file_name="C:\news\travel"  this will not work 

file_name = r"C:\news\travel"
print(file_name)  #r in here is raw string it will ignore escape charecters


some_random_number=5
some_obsure_calculation=25
some_additional_statistic_fetched_from_somewhere=10

# use \ to maintain the line size or minimize lenthy expressions. 

final= some_random_number + \
    some_obsure_calculation + \
    some_additional_statistic_fetched_from_somewhere

print(some_additional_statistic_fetched_from_somewhere,
      some_obsure_calculation,
      some_random_number)
