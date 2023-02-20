powerball_numbers = [4, 8,15,16, 23, 42]

#Mysol
def squares(num1):
    nw_lst = []
    for intx in num1:
        #nw_lst.append(intx * intx)
        nw_lst.append(intx ** 2)
    return nw_lst

#givensol
# --same as mine 


print(squares(powerball_numbers)) #16 64 ...



def convert_to_floats(numbers):
    nw_lst = []
    for intx in numbers:
        #nw_lst.append(intx * intx)
        nw_lst.append(float(intx))
    return nw_lst

#givensol
# --same as mine 

print(convert_to_floats(powerball_numbers))
print(convert_to_floats([100, 200, 300]))


def even_or_odd(numbers):
    nw_lit = []
    for indx in numbers:
        if indx % 2 == 0:
            nw_lit.append(True)
        else:
            nw_lit.append(False) 
    return nw_lit

#givensol
# --same as mine 

print(even_or_odd(powerball_numbers))   