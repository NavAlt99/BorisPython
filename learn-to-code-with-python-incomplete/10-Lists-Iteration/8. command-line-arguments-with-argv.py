import sys

# print(sys.argv)
# print(type(sys.argv))

word_lengths = 0 

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"The total lenght of all command-line argumetns is {word_lengths}")

#to trunn the script in terminal || python '.\8. command-line-arguments-with-argv.py' hello goodbye python || 