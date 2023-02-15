# print (3 in [1, 2, 3, 4, 5])


def contains(vals, trgt):
    found = False
    for val in vals:
        print(val)
        if val == trgt:
            found = True 
            break
    return found 

print(contains([1, 2, 3, 6, 7], 2))