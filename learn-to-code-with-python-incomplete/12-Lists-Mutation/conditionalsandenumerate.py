# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

#Mysolution
def length_match (strg1, num1):
    counter = 0
    for word in strg1:
        if len(word) == num1:
            counter += 1
    return counter

#Given solution
# -- same as my solution


# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42


        



def sum_from(numx, numy):
    cntr = 0
    if numy > numx:
        while numy > numx:
            cntr += numx
            numx +=1
    else:
        print("Second number must be greater than first")
    return cntr+numx


#Given solution
def sum_from(start, end):
    total = 0
    for number in range(start, end + 1 ):
        total += number
    return total 





# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions 
# in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(lst1, lst2):
    results = []
    
    for index, value in enumerate(lst1):
        if lst2[index] == value:
            results.append(index)
    
    return results




