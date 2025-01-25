# Strings
a = "Hello, World!"
name = 'John'
print(name)

# String Slicing 
print(name[0:3]) # 0 to 3 but not 3 
print(name[0:3:1]) # 0 to 3 but not 3 with step 1

# String Functions 
print(len(name)) # returns length of string 
print(name.lower()) # returns lower case of string
print(name.upper()) # returns upper case of string
print(name.replace('J', 'K')) # replaces J with K in string
print(name.startswith('J')) # returns True if string starts with J
print(name.endswith('n')) # returns True if string ends with n
print(name.find('o')) # returns index of first occurence of o

# Escape Sequences 
print("Hello\nWorld!") # \n is used for new line
print("Hello\tWorld!") # \t is used for tab
print("Hello\\World!") # \\ is used for backslash
print("Hello\"World!") # \" is used for double quote
print("Hello\'World!") # \' is used for single quote

