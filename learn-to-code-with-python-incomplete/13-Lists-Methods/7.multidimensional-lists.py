bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# print(len(bubble_tea_flavors))
# print(len(bubble_tea_flavors[0]))
# print(bubble_tea_flavors[0])
# print(bubble_tea_flavors[1])
# print(bubble_tea_flavors[-1])

# print(bubble_tea_flavors[1][2])
# print(bubble_tea_flavors[0][0])
# print(bubble_tea_flavors[2][1])

all_flavours = []
for flavour_pack in bubble_tea_flavors:
    print(flavour_pack)
    for flavour in flavour_pack:
        all_flavours.append(flavour)


print(all_flavours)
