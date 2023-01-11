def positive_or_negative(num):
    if num > 0:
        return "Positive!"
    elif num < 0:
        return "Negative!"
    else:
        return "Neither!"

print(positive_or_negative(0))
print(positive_or_negative(-5))
print(positive_or_negative(5))

def calculator(operation, a,b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "I don't know what you want me to do!"
    
print(calculator("multiply", 100,9))
print(calculator("add", 100,9))
print(calculator("subtract", 100,9))
print(calculator("divide", 100,9))
print(calculator("transmogrify", 100,9))

