# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120

# def factorial(num):
#     final_num = num
#     while num >= 1:
#         final_num = final_num * num
#         num -=1
#     print(final_num)

# 1 * 5 = 5 
# 5 * 4 = 20
# 20 * 3 = 60
# 60 * 2 = 120
# 120 * 1 = 120 


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return  num * factorial(num -1)

    
print(factorial(5))