# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0


def nested_sum(lst_lists):
    sum = 0
    for lt in lst_lists:
        for numx in lt: 
            sum += numx
    return sum




# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""


# def fancy_concatenate(lst_listx):
#     string_list = []
#     stringx = ""
#     for ltx in lst_listx:
#         if len(ltx) == 3:
#             for charx in ltx:
#                 string_list.append(charx)
#     return stringx + ("".join(string_list))

def fancy_concatenate(lst_listx):
    stringx = ""
    for ltx in lst_listx:
        if len(ltx) == 3:
            for charx in ltx:
                stringx += charx
    
    return stringx

print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F","G"]]))            