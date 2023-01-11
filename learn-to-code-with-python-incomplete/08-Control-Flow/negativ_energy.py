# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(num1):
    if num1 < 0:
        return num1 * -1
    elif num1 > 0:
        return num1
    else:
        num1 == 0
        return 0


print(negative_energy(-100))