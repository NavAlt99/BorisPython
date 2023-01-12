def add(a, b):
   return a+b
   print("blah")  #this statement will never run as function stops executing after return statement is encounterd 


result = add(3, 5)
print(type(result))
print(result)


def convert_to_currency(a):
    return "$"+str(a)
    
blah=convert_to_currency(15)

print(blah)