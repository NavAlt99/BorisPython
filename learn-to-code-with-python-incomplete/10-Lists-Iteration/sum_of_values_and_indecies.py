# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1


def in_list(lststr, str1):
    if str1 in lststr:
        return lststr.index(str1)
    else:
        return -1 

def in_list2(strings, target):
    for index, element in enumerate(strings):
        if element == target:
            return index
        else:
            return -1 


# strings = ["enchanted", "sparks fly", "long live"]
# print(in_list(strings, "enchanted") )
# print(in_list(strings, "sparks fly"))
# print(in_list(strings, "fifteen"))
# print(in_list(strings, "love story"))


# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(list1):
    idx = 0
    sum = 0
    total = 0
    for i in list1:
        sum = idx + i 
        idx += 1 
        total += sum
    return total


# print(sum_of_values_and_indices([1, 2, 3]) )
# print(sum_of_values_and_indices([0, 0, 0, 0]))
# print(sum_of_values_and_indices([]) )

def sum_of_values_and_indices2(values):
    total = 0

    for index, number in enumerate(values):
        total += index + number

    return total









