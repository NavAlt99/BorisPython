# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]



# def factors(numy):
#     nw_list = []
#     ctrlnum =  1
#     while numy  >= ctrlnum:
#         if (numy % ctrlnum) == 0:
#             nw_list.append(ctrlnum)
#             ctrlnum += 1
            
#     return nw_list


def factors(numx):
    nw_list = [] 

    for i in range(1, numx +1):
        if numx % i == 0:
            nw_list.append(i)
    
    return nw_list


print(factors(64)) 
