# default arguments are fallback arguments that are passed to a function if * -
# *- an explicit value is not provided for a parameter. 



def add(a = 0, b = 0):
    return a + b 

print(add(7, 8))
print(add(7))
print(add())




