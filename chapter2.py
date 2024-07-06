# # a=2
# # b=3
# # print(a+b)


# # codechef solution 
# # t=int(input())
# # print((t-1)*3+4)


# # datatype
# a=1 #a is the integer type
# b=4.23 #b is a floting 
# c="hello" #c is a string type



# # ####Rules for Variable Names


# # Must Start with a Letter or Underscore:
# # A variable name must begin with a letter (a-z, A-Z) or an underscore (_).
# # Examples: name, _value, score
# # Cannot Start with a Number:

# # Variable names cannot begin with a number.
# # Invalid Example: 2nd_value (Incorrect)
# # Can Only Contain Alphanumeric Characters and Underscores:

# # Variable names can contain letters, numbers, and underscores.
# # Valid Examples: total_score, value2, name_age
# # Case-Sensitive:

# # Variable names are case-sensitive. age and Age are different variables.
# # Example: Name, name, and NAME are considered different variables.
# # Cannot Use Python Keywords:

# # You cannot use reserved words in Python as variable names. These are words that have special meaning in Python.
# # Example of keywords: and, if, else, class, try, etc.
# # Example: if = 5 (Invalid)
# # Avoid Special Characters:

# # Avoid using special characters like @, #, $, %, etc., in variable names.
# # Invalid Example: user@name (Incorrect)
# # Best Practices for Variable Names
# # Use Descriptive Names:

# # Choose variable names that are descriptive and convey the purpose of the variable.
# # Example: Use total_score instead of ts.
# # Use Lowercase Words with Underscores for Readability:

# # For multi-word variable names, use underscores to separate words.
# # Example: first_name, last_name, total_price
# # CamelCase for Class Names:

# # Use CamelCase (e.g., MyClassName) for naming classes, not for variables.
# # Example: StudentRecord, EmployeeDetails
# # Constants in All Uppercase:

# # Use all uppercase letters with underscores to define constants (variables that should not change).
# # Example: MAX_LIMIT, PI_VALUE
# # Avoid Single-Letter Names:

# # Avoid using single letters like x, y unless they are used as loop counters or in contexts where the purpose is clear.
# # Example: Use index instead of i for a loop variable when possible.
# # Do Not Shadow Built-In Functions:

# # Avoid naming variables with the same names as built-in Python functions or standard library modules.
# # Example: Do not use list, dict, max, min as variable names.
# a=5<4
# print(a)

# #logical operators
# e=True or False
# #truth table of or
# print("true or false is ",True or False)
# print("false or true is ",False or True)
# print("true or true is ",True or True)
# print("false or false is ",False or False)

# e=True and False
# #truth table of or
# print("true  and false is ",True  and False)
# print("false and  true is ",False and True)
# print("true  and true is ",True   and True)
# print("false and  false is ",False and  False)

# #type function
# a=2
# t=type(a)
# print(t)
# b=54.45
# t=type(b)
# print(t)
# b="ravi kumar"
# t=type(b)
# print(t)
# x=45.5
# y=float(x)
# z=type(x)
# print(y)
# print(z)


# vvi  when int is not used at input the program work at string
# so sum of 1 and 2 in 12
a=int(input())
b=int(input())
print("number of a is " , a)
print("number of a is " , b)
print("sum of two number ",a+b)
rem=a%b
print("remainder of thies number " , rem)
print("statement  is true or false  " , a<b)
print("average of the two number  " , (a+b)/2)
print("square of the  number  " ,pow(a,2) )
print("square of the  number  " ,a**2 )