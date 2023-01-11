# A list is a data structure that stores an ordered sequence of objects, a list is an object that stores 
# objects in an order, a list can also be called an array. 
# [] is an example of a literal 

empty = [] # [] represent a list and being assigned to a variable called empty
empty = list() # list() is a built in list function syntax in line 5 is preferred, 
#list() function can be used to convert another object to list

sodas = ["COKE", "PEPSI", "FANTA"] # list is not just container for three elements here, its container for 
# three elements in order starting from zero

print(sodas[1])
print(len(sodas))


quarterly_revenue = [15000, 12000, 9000, 20000]
print(len(quarterly_revenue))

stock_prices = [343.25, 420.21, 500.96]
print(len(stock_prices))

user_settings = [True, False, False, True, False, 1, "Hello"]

print( len(user_settings))
