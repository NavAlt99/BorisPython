# count = 0

# while count <=5:
#     print(count)
#     count += 1

# print(count)

# while count <=5:
#     print(count)
#     count += 1


# invalid_number = True

# while invalid_number:
#     user_value = int(input("Please enter a number above 10: "))
#     if user_value > 10:
#         print(f"Thanks, that works! {user_value} is a great choice!")
#         invalid_number = False
#     else:
#         print("That doesn't fit ! Try, again!")



count=1

while count <=30:
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count+=1