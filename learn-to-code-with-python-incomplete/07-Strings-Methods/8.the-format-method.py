# name, adjective, noune
mad_libs="{} laughed at the {} {}."

print(mad_libs.format("Boris","Red","alien"))
print(mad_libs.format("Jennifer","Silly","tomato"))
# print(mad_libs.format("Jennifer","Silly")) will return indexError as insufficient arguments

print()
mad_libs="{2} laughed at the {1} {0}."
print(mad_libs.format("Boris","Red","alien"))
print(mad_libs.format("Jennifer","Silly","tomato"))

print()
mad_libs="{name} laughed at the {adjective} {noun}."
print(mad_libs.format(name="Boris",adjective="Red",noun="alien"))
print(mad_libs.format(name="Jennifer",adjective="Silly",noun="tomato"))

print()
mad_libs="{name} laughed at the {adjective} {noun}."
name=input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective= adjective, noun= noun ))