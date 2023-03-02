#!/bin/python

# List of ten string elements
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "indian gooseberry", "jackfruit"]


print("Fourth element of the list:", my_list[3])
print("Sixth through tenth element of the list:", my_list[5:])

my_list[6] = "onion"

# Updated list
print("Updated list:", my_list)


# Stretch Goals

# Create a list of strings
my_list = ['apple', 'banana', 'cherry', 'date']

# Append an element to the end of the list
my_list.append('elderberry')
print(my_list)  

# Clear all the elements from the list
my_list.clear()
print(my_list)  

# Create a new list and copy it
my_list = ['apple', 'banana', 'cherry', 'date']
my_list_copy = my_list.copy()
print(my_list_copy)  

# Count the number of times an element appears in the list
my_list = ['apple', 'banana', 'cherry', 'date', 'banana']
count = my_list.count('banana')
print(count)  

# Extend the list with elements from another list
more_my_list = ['elderberry', 'fig']
my_list.extend(more_my_list)
print(my_list)  

# Get the index of an element in the list
index = my_list.index('cherry')
print(index)  # Output: 2

# Insert an element at a specific index in the list
my_list.insert(1, 'cantaloupe')
print(my_list)  

# Remove and return the last element from the list
last_fruit = my_list.pop()
print(last_fruit)  
print(my_list) 

# Remove the first occurrence of an element from the list
my_list.remove('banana')
print(my_list)  

# Reverse the order of the elements in the list
my_list.reverse()
print(my_list)  

# Sort the elements in the list in ascending order
my_list.sort()
print(my_list)  
