meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("fast" in meals)
print("snack" in meals)
print("dinner" in meals)
print("breakfast" in meals)

print()

test_scores = [99.0, 88.01, 32.5]
print(99 in test_scores)
print(99.0 in test_scores)
print(88 in test_scores)
print(32 in test_scores)
print(88.01 in test_scores)

print()
print("\"Not In\"")

print("lunch" not in meals)
print("Breakfast" not in meals)
print(1000 not in test_scores)
print(99 not in test_scores)


if 1000 not in test_scores:
    print("The value is not in there")