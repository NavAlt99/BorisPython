def add(a, b, c):
    print("The sume of all three arguments is", a+b+c)


add(2, 4, 6)

#keyword parameters or argumetns 
add(a=4, b=6, c=3)
add(b=4, a=4, c=15)

# mix match possitional arguments with keyword arguments 
add(5, c=15, b=100)
