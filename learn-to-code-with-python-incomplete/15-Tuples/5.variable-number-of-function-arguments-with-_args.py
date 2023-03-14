def accept_stuff(*args):
    print(type(args))
    print(args)


accept_stuff(1)
accept_stuff(1, 3, 5)
accept_stuff()


def my_max(nonsense, more_nonsense, *numbers):
    print(nonsense)
    print(more_nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print()
print(my_max("Shazam", 1, 1))
print(my_max("Blah", 1, 3))
print(my_max("Leo", 1, 3, 9, 6, 7, 8, -14))