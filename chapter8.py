#function concept in python 
#function create,,definition;
# def avg():
#           a=int(input("enter the first number:"))
#           b=int(input("enter the second number:"))
#           c=int(input("enter the third number:"))

#           average = (a+b+c)/3
#           print(average)
          #function call 
# avg()
#question 
# def goodday():
#         print("good day")
# goodday()

#function with argument 
# def goodday(name,ending):
#         print("good day ,"+ name)
#         print(ending)

# goodday("Ravi","Thank You")
# goodday("Rocky","Thank You")
# goodday("Rahul ","Thanks")
#return value concept
# def goodday(name,ending):
#         print("good day ,"+ name)
#         print(ending)
#         return "return value concept"
# a=goodday("Ravi","Thank You")
# print(a)


#default argument concept
# def goodday(name="Ravi",ending="Thank You"):
#         print("good day ,"+ name)
#         print(ending)
#         return "return value concept"
# a=goodday("Ravi","Thank You")


#recursion function 
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# n=int(input("enter the number : "))
# print(f"the value of the factorial number: ",factorial(5))


#find faranhight to celcious
# def f_to_c(f):
#           return 5*(f-32)/9
# f=int(input("enter the farenheight : "))
# c=f_to_c(f)
# print(f_to_c(f))


# def sum(n):
#         if n==1:
#                 return 1
#         else:
#                 return n+sum(n-1)
# n=int(input("enter the number : "))
# print(sum(n))

#pattern code i python
# def pattern(n):
#           if(n==0):
#                   return 
#           print("*"*n)
#           pattern(n-1)
# pattern(5)


# vvi conceptions
# def rem(l,word):
#           for item in l:
#                   l.remove(word)
#                   return l
# l= ["ravi","rahul","rocky","an"]
# print(rem(l,"an"))

#strinp function it remove word start and end at anty position 
def rem(l,word):
          n=[]
          for item in l:
                 if not(item==word):
                    n.append(item.strip(word))
          return n
l= ["ravi","rahul","rohan","rocky","an"]
print(rem(l,"an"))
