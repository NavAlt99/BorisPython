import sys

# print(sys.argv)
# print(type(sys.argv))

word_lengths = 0 

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"The total lenght of all command-line argumetns is {word_lengths}")

#to trunn the script in terminal || python '.\8. command-line-arguments-with-argv.py' hello goodbye python || 



# What makes a list an iterable object? What is another example of an iterable object?
# * An object is iterable if its elements can be accessed one at a time. A string is another iterable object — its characters can be accessed one at a time.

# What is an alternative syntax to using the reversed function to iterate backwards over a list?
# * The special slice syntax ​[::-1]​ returns a copy of the list with the elements in reverse order.

# What function allows us to access the index of each element in the for loop?
# * The enumerate function grants access to the index of each element in a for loop. It will be represented by the first of the two variables we place after the for keyword.

# What is the difference between the break and continue keywords?
# * The continue keyword moves the loop to the start of the next iteration. The break keyword terminates the loop completely.

# What do the three arguments to the range function present?
# * The inclusive starting value, the exclusive ending value and the stride interval.