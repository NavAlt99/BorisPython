# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

def sum_of_lengths(strlist):
    total_len=0
    for strlen in strlist:
        total_len = total_len + len(strlen)
    return total_len



# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10


def product(numbers):
    producto = 1
    for number in numbers:
        producto = producto * number
    return producto


print(product([4, 5, 6, 7]))