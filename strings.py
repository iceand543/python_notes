print("strings are easy to use")
print('strings are fun')
print("testing the 'string'")
print('testing "string"')
print("string" + "concatenation")

greeting = "hello"
name = "laks"

print(greeting+ ' ' +name)

# input_name = input("enter your name")
# age = input("what's your age")
# print(input_name + "'s age is",age)
# when you use comma, it just acts as a space.
# Use + instead to concatenate.
# literal is any value of type. For example, "text sample", 6 are literals of different data types
# String data type can be called a sequence type

#------------------------------------------------------------------------------------------------------------
#string index
parrot = "some sameple text"
print(parrot[1])
print(parrot[-1])

# string slicing
print(parrot[1:4]) # it would slice upto index 3 but not include 4
print(parrot[:4]) # prints from 0 index
print(parrot[1:]) # prints until last index
print(parrot[-4:-2])

# string step
print(parrot[1:6:2])# two here is the interval
number = "1,234,543:324,234;234.32"
separators = number[1::4]
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
# using negative step value, you can print the string backwards