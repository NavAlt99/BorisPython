if 5 < 7 and "rain" == "rain":
    print("Both of the condistions evaluate to True")

if 5 < 7 and "rain" == "fire":
    print("This will not print because at least one of the two condistions is false")

if "rain" == "fire" and 5 < 7:
    print("This will not print because at least one of the two condistions is false")

if "rain" == "fire" and 5 < 3:
    print("This will not print because at least one of the two condistions is false")


value = 95

# if value > 90 and value < 100:
if 90 < value < 100:
    print("This is a shortcut for the win!")    


