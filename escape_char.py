sample_string = "akfhalhflakskdhflk\nnfd,s.nads.,,n\ndhfkhskdf\thkshd"
print(sample_string)
#\n newline
#\t tabspace
#\ can be use to escape any special characters, example is below
print("\"pet shop owner said something that i don't care\"")
# alternate to above way is useing """
print(""" "pet shop owner said something that i don't care" """)

split_string = """first line
second line
third line 
                    """
print(split_string)
# in other case, if you don't want to have long lines of strings, you can use \ at the end of the line
Continue_string = """first line \
second line \
third line \
"""
print(Continue_string)
# What id we want to use \ in our string?
backslash_string = "my name is lakshmi chekuri and my date of birth is 16\05\1993"
# you can fix the above problem by adding one more back slash to the existing one
backslash_string2 = "my name is lakshmi chekuri and my date of birth is 16\\05\\1993"
# othe rway is using raw strings
backslash_string3 = r"my name is lakshmi chekuri and my date of birth is 16\05\1993"
print(backslash_string)
print(backslash_string2)
print(backslash_string3)