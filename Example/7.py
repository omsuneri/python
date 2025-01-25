# Lists in python   
name = ['John', 'Doe', 25]
value = [5, 6, 4, 3, 2, 1]
print(name)

# List Slicing and indexing 
print(name[0:2]) # 0 to 2 but not 2
print(name[0]) # 0th index element

# List Functions
print(len(name)) # returns length of list
print(name.count('John')) # returns count of John in list
print(name.index('Doe')) # returns index of Doe in list
name.insert(1, "om") # inserts Smith at 1st index
value.sort() # sorts the list
value.reverse() # reverses the list
print(value)
value.pop(2) # removes last element
print(value)
value.remove(2) # removes 4 from list
print(value)