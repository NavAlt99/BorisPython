# Recurssion is a challanging idea in programming. Recursion forces our brains to think in 
# multiple dimentions to keep track of multiple operations running 
# Recursion is when a fucntion that we built calls itself whithin its own
#  *** When a function calls itself ***

# Before we even finsh  defining the body of a function, we can actually go ahead and invoke that exact
# same function within the body or the block of the function that we are currently defining.
# If you think about it, we can invoke any other function within the body of a function.

# We've written plenty of code in this in this class, in this course, where we have defined our own 
# custom function and invoked another function like print or land within the body. It's the exact same idea, 
# except we can invoke the function that we are currently inside in.

## done without recursion
# def count_down_from(num):
#     start = num
#     while start > 0:
#         print(start)
#         start -= 1

# count_down_from(5)

## using recursion
def count_down_from(num2):
    if num2 < 0:
        return
    print(num2)
    count_down_from(num2 - 1)



count_down_from(5)