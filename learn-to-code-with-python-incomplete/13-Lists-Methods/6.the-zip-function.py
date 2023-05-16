breakfasts = ["Eggs", "Oats", "Apple"]
lunches = ["Subway", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

# print(zip(breakfasts, lunches, dinners))
# print(type(zip(breakfasts, lunches, dinners)))
# print(list(zip(breakfasts, lunches, dinners)))

for  bfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f" My meal for today was {bfast} and {lunch} and {dinner}.")


for a, b, c in zip([3, 2, 1], [1, 2, 3], [2, 3, 1]):
    print("*-*".join([str(a), str(b), str(c)]))

print("!".join(["Who", "let", "the", "dogs", "out?"]))

