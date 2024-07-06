# #list method 
# group =["ravi","rahul","rockey",24057,24.24,False,"prince"]
# print(group)
# group.append("pnea")
# print(group)
# group.insert(2,"prince")
# print(group)
# group[0]="RAVI"
# print(group)
# # Create a list
# fruits = ['apple', 'banana', 'cherry']

# # Append an element
# fruits.append('orange')
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# # Insert an element
# fruits.insert(1, 'blueberry')
# print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# # Extend the list
# fruits.extend(['grape', 'kiwi'])
# print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'grape', 'kiwi']

# # Remove an element
# fruits.remove('banana')
# print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'grape', 'kiwi']

# # Pop an element
# removed_fruit = fruits.pop(2)
# print(removed_fruit)  # Output: 'cherry'
# print(fruits)  # Output: ['apple', 'blueberry', 'orange', 'grape', 'kiwi']

# # Get the index of an element
# index_of_grape = fruits.index('grape')
# print(index_of_grape)  # Output: 3

# # Count occurrences
# num_apples = fruits.count('apple')
# print(num_apples)  # Output: 1

# # Sort the list
# fruits.sort()
# print(fruits)  # Output: ['apple', 'blueberry', 'grape', 'kiwi', 'orange']

# # Reverse the list
# fruits.reverse()
# print(fruits)  # Output: ['orange', 'kiwi', 'grape', 'blueberry', 'apple']

# # Copy the list
# fruits_copy = fruits.copy()
# print(fruits_copy)  # Output: ['orange', 'kiwi', 'grape', 'blueberry', 'apple']

# # Clear the list
# fruits.clear()
# print(fruits)  # Output: []



#initialies tuble in python
a=(1,23,45,"wefa","lksjdh",False)
print(a)
#.count():
print(a.count(45))
#.index():
print(a.index(False))
# len():
my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Output: 4
# max():
numbers = (1, 2, 3, 4)
print(max(numbers))  # Output: 4
# min():
numbers = (1, 2, 3, 4)
print(min(numbers))  # Output: 1
# sum():
numbers = (1, 2, 3, 4)
print(sum(numbers))  # Output: 10
# sorted():
numbers = (4, 1, 3, 2)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
# all():
values = (1, 2, 3)
print(all(values))  # Output: True
# tuple():
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
# zip():
names = ('Alice', 'Bob')
scores = (85, 90)
combined = tuple(zip(names, scores))
print(combined)  # Output: (('Alice', 85), ('Bob', 90))
# enumerate():
items = ('apple', 'banana', 'cherry')
enumerated_items = tuple(enumerate(items, start=1))
print(enumerated_items)  # Output: ((1, 'apple'), (2, 'banana'), (3, 'cherry'))



# example for all test function in tuple
# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 20)

# Using count() to count occurrences of 20
count_20 = my_tuple.count(20)
print(f"20 occurs {count_20} times")  # Output: 20 occurs 3 times

# Using index() to find the first occurrence of 20
index_20 = my_tuple.index(20)
print(f"First occurrence of 20 is at index {index_20}")  # Output: First occurrence of 20 is at index 1

# Using len() to get the length of the tuple
length = len(my_tuple)
print(f"Length of the tuple: {length}")  # Output: Length of the tuple: 6

# Using max() to find the maximum value
maximum = max(my_tuple)
print(f"Maximum value: {maximum}")  # Output: Maximum value: 40

# Using min() to find the minimum value
minimum = min(my_tuple)
print(f"Minimum value: {minimum}")  # Output: Minimum value: 10

# Using sum() to sum all elements
total = sum(my_tuple)
print(f"Sum of all elements: {total}")  # Output: Sum of all elements: 140

# Using sorted() to get a sorted list from the tuple
sorted_tuple = sorted(my_tuple)
print(f"Sorted tuple: {sorted_tuple}")  # Output: Sorted tuple: [10, 20, 20, 20, 30, 40]

# Using all() to check if all elements are true
all_true = all(my_tuple)
print(f"All elements are true: {all_true}")  # Output: All elements are true: True

# Using any() to check if any element is true
any_true = any(my_tuple)
print(f"Any element is true: {any_true}")  # Output: Any element is true: True

# Using tuple() to convert a list to a tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
print(f"Converted tuple: {converted_tuple}")  # Output: Converted tuple: (1, 2, 3)

# Using zip() to combine two tuples
names = ('Alice', 'Bob')
scores = (95, 85)
combined = tuple(zip(names, scores))
print(f"Zipped tuples: {combined}")  # Output: Zipped tuples: (('Alice', 95), ('Bob', 85))

# Using enumerate() to enumerate a tuple
fruits = ('apple', 'banana', 'cherry')
enumerated_fruits = tuple(enumerate(fruits))
print(f"Enumerated fruits: {enumerated_fruits}")  # Output: Enumerated fruits: ((0, 'apple'), (1, 'banana'), (2, 'cherry'))
