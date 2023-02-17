
# def reverse(str):
#     str_len = len(str)-1
#     while str_len >= 0:
#         print(str[str_len])
#         reverse(str[str_len-1])

# reverse("Spring") #"does not work"


# def reverse(str):
#     start_index = 0
#     last_index = len(str) -1 
#     reverse_string = ""

#     while last_index >= start_index:
#         reverse_string = reverse_string + str[last_index]
#         last_index -= 1
#     return reverse_string


def reverse(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + reverse(str[:-1])



print(reverse("Spring"))

# Spring
# g + reverse(Sprin)
# g + n + reverse(Spri)
# g + n + i + reverse(Spr)
# g + n + i + r + reverse(Sp)
# g + n + i + r + p reverse(S)
# g + n + i + r + p + S
#
#
#