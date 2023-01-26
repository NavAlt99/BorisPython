errands = ["Go to gym", "Wash utinsils", "Clean Kitchen", "Get Promoted at work", "Sleep"]

#print(enumerate(errands))

for index, chore in enumerate(errands, 1): # starts index from 1
    print(f"{chore} is number {index } on my list of things to do today!")