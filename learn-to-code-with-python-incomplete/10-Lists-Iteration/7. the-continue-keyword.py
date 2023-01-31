# def sum_of_positivie_numbers(values):
#     total = 0

#     for val in values:
#         if val > 0:
#             total += val
#     return total

def sum_of_positivie_numbers(values):
    total = 0 

    for val in values:
        if val < 0:
            continue

        total += val
    
    return total



print(sum_of_positivie_numbers([1, 2, -3, 4]))





