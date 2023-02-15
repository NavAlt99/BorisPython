alphabet="abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2]) #jumps with increments of 2 
print(alphabet[0::3]) #jumps with increments of 3, by default it will end at last if left empty
print(alphabet[:26:3]) # by default it will start from 0 if left empty
print(alphabet[::3]) # by default it will start from 0 if left empty and ends at last if let empty
print(alphabet[4:20:5])
print(alphabet[-20:-8:5])
print(alphabet[::-1])#if negative integer is given at the end starts from the last and moves three steps backword
print(alphabet[::-3]) 
print(alphabet[:19:-1])
print(alphabet[-5:])

