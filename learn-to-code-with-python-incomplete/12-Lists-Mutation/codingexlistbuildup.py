# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []


def only_evens(fu_list):
    nw_list = []
    for num in fu_list:
        if num % 2 == 0:
            nw_list.append(num)
    
    return nw_list 

print(only_evens([4, 8, 15, 16, 23, 42]))


# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []


def long_strings(foo_list):
    nw_list = []
    for str in foo_list:
        if len(str) >= 5:
            nw_list.append(str)
    
    return nw_list

print(long_strings(["Hello", "Goodbye", "Sam"]))