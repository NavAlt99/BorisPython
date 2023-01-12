# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(list2):
    counter = list2[0]
    for item2 in list2:
        if item2 < counter:
            counter = item2
    return counter


# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""


def concatenate(strlist):
    returnstr = ""
    for item in strlist:
        if len(item) > 2:
            returnstr = returnstr + item
    return returnstr

print(concatenate(["abc", "def", "ghi"]))



# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12


def super_sum(strlist):
    index = 0
    returnval = 0 
    for s in strlist:
        if "s" in s:
            index = s.index("s")
            returnval += index
    return returnval


print(super_sum([]))
print(super_sum(["mustache"]) )
print(super_sum(["mustache", "greatest"]) )


