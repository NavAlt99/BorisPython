# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]


def word_lengths(stringx):
    new_list =[]
    for wrd in stringx.split(" "):
        new_list.append(len(wrd))
    
    return new_list




# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup(listx):
    clean_strg = []
    for strg in listx:
        if strg.isspace() or len(strg) == 0:
            continue

        clean_strg.append(strg)

    return (" ".join(clean_strg))

print(cleanup(["cat", " ", "er", "", "pillar"]))

