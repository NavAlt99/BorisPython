# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []


# def right_words(list_w, num):
#     rturn_list = []
#     for word in list_w:
#         if len(word) == num:
#             rturn_list.append(word)
#     return rturn_list

def right_words(list_w, num):
    return list(filter(lambda word: len(word) == num, list_w))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))



# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []

def only_odds(list_wholenum):
    retrn_list = []
    for num in list_wholenum:
        if num % 2 != 0:
            retrn_list.append(num)
    return retrn_list

# print(only_odds([1, 3, 5, 6, 7, 8]))


# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])    


# def count_of_a(list_string):
