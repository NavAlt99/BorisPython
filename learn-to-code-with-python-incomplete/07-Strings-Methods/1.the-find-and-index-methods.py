# Method is a function that acts upon a specific object, It's an action or procedure that you can take on a specific object. 
# Its a command or instruction that you can give. Much like function methods are invoked. 
# much like functions they can accept arguments and return values. 



browser= "Google Chrome"
print(browser.find("C"))
print(browser.find("Ch")) # we are going to get starting position of the pattern
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("z")) # going to return -1, i.e going to be consistant return value for not found
print(browser.find("zxy"))


print()

print(browser.find("o"))
print(browser.find("o",2))
print(browser.find("o",5)) #returns index position of the string not the index position from 5

print("Ch" in browser) # If you want to get a boolean value if a character or pattern in a string

print(browser.index("C"))
# print(browser.index("Z")) returns a ValueError 

print(browser.rfind("G"))

print ( "nerds are nerds for ever".rfind( "nerds",9) )

word = 'geeks for gaeks'
print(word.rfind('ge',0))