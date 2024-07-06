# #  #dictoneries in pythan
# # marks={
# #           "ravi":100,
# #           "rocky":67,
# #           "rahul":100,
# #           0:"harry"
# # }
# # marks.update({"ravi": 99,"renuka":100})
# # print(marks)

# # dict.clear()
# name = {'name':"ravi","age": 24}
# print(name.clear())


# # dict.copy()
# name = {'name':"ravi","age": 24}
# print(name.copy())

# # dict.fromkeys() vvi
# keys = ['name', 'age', 'location']
# x = 'unknown'
# y= dict.fromkeys(keys, x)
# print(y)  # Output: {'name': 'unknown', 'age': 'unknown', 'location': 'unknown'}

# # Creating a dictionary
# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # Using get() to access values
# name = my_dict.get('name')
# print(f"Name: {name}")  # Output: Name: Alice

# # Using keys() to get a list of keys
# keys = my_dict.keys()
# print(f"Keys: {list(keys)}")  # Output: Keys: ['name', 'age', 'city']

# # Using values() to get a list of values
# values = my_dict.values()
# print(f"Values: {list(values)}")  # Output: Values: ['Alice', 25, 'New York']

# # Using items() to get a list of key-value pairs
# items = my_dict.items()
# print(f"Items: {list(items)}")  # Output: Items: [('name', 'Alice'), ('age', 25), ('city', 'New York')]

# # Using update() to add new key-value pairs
# my_dict.update({'country': 'USA', 'phone': '123-4567'})
# print(f"Updated dictionary: {my_dict}")
# # Output: Updated dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA', 'phone': '123-4567'}

# # Using pop() to remove a key-value pair
# removed_value = my_dict.pop('age')
# print(f"Removed value: {removed_value}")  # Output: Removed value: 25
# print(f"Dictionary after pop: {my_dict}")

# # Using popitem() to remove the last key-value pair
# last_item = my_dict.popitem()
# print(f"Last item removed: {last_item}")
# print(f"Dictionary after popitem: {my_dict}")

# # Using setdefault() to get a value or set a default if key is missing
# city = my_dict.setdefault('city', 'Los Angeles')
# print(f"City: {city}")  # Output: City: New York

# # Using fromkeys() to create a new dictionary with default values
# keys = ['x', 'y', 'z']
# default_value = 0
# new_dict = dict.fromkeys(keys, default_value)
# print(f"New dictionary: {new_dict}")

# # Using clear() to remove all items from the dictionary
# my_dict.clear()
# print(f"Dictionary after clear: {my_dict}")  # Output: Dictionary after clear: {}









# s={1,2,2,3,4,5,5,6,6,7,}
# print(s)
# # create a empty set
# e=set()
# print(e)
# s1={1,2,4,6,8}
# s2={23,34,1,6,2}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

# practice problem of python     
words={
          "madad":"help",
          "kuuta":"dog",
          "billi":"cat",
          "haathi":"elephant"
}
word=input("Enter the word you want meaning of :")
print(words[word])
# vvvvvvvvvviiiiiiiii
s=set()
s.add(1)
s.add(1.0)
s.add("1")
print(s)
print(len(s))

d={}
name=input("enter the friend name:")
lang = input("Enter the language of the friend :")
d.update({name: lang})
name=input("enter the friend name:")
lang = input("Enter the language of the friend :")
d.update({name: lang})
name=input("enter the friend name:")
lang = input("Enter the language of the friend :")
d.update({name: lang})
name=input("enter the friend name:")
lang = input("Enter the language of the friend :")
d.update({name: lang})
print(d)