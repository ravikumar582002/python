# # conditional expression  if elif else conditional
# a=int(input("Enter your age : "))
# #start the statement 1
# if(a%2==0):
#         print("a  is even number")
#         #End of statement 1;
#         #start the statement 2
# if(a>20):
#           print("You are eligible for voting")
#           print("go for voting") 
# elif(a==20):
#           print("You are eligible for voting")
# else:
#         print("you are not elegable for voting ")


# print("End the program ")
#practic set
#question number 1;
# a1=int(input(" Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))
# if(a1>a2 and a1>a3 and a1>a4):
#           print ("greater number is a1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#           print("greater number is a2: ",a2)
# elif(a3>a2 and a3>a1 and a3>a4):
#           print ("greater number is a1: ",a1)

# if(a4>a1 and a4>a3 and a4>a2):
#           print("greater number is a2: ",a2)

#           #question 2
# marks1=int(input("Enter marks 1: "))
# marks2=int(input("Enter marks 2: "))
# marks3=int(input("Enter marks 3: "))
# total_pecentage =int((100*( marks1+ marks2+ marks3))/300)
# if(total_pecentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#           print("you are pass",total_pecentage)
# else:
#           print("you are fail",total_pecentage)

# post= input("enter the post: ")
# if("RAVI" in post.upper()):
#         print("This post is talking about ravi ")
# else:
#         print("This post is not talking about ravi ")
# loop concept:
# print(1)
# print(2)
# print(3)
# for i in range(1,6):
#           print(i)
# i=1
# while(i<5):
#           print(i)
#           i+=1
#           list=["ravi",False,'shone',"shubham","shubhi"]
#           i=0
# while(i<len(list)):
#           print(list[i])
#           i+=1
# word = ["ravi",'shone',"shubham","shubhi","rahul"]
# for name in word:
#           if(name.startswith("s")):
#                   print(f"hello {name}")

# word = ["ravi",'shone',"shubham","shubhi","rahul"]
# i=0
# while(i<=len(word)):
#           if(word[i]=="s"):
#                   i+=1
#                   print(f"hello {word}")
#find the prime number 
# n=int(input("enter a number :"))
# for i in range(2,n):
#         if(n%i==0):
#                 print("number is not a prime number ")
#                 break
# else:
                # print("number is a prime number ")

                # #using while loop to find the prime numjber
                # n=int(input("enter a number :"))
                # i=1
                # sum=0
                # while(i<n):
                #         sum+=i
                #         i+=1
                #         print(sum)
                        # factorial of given number
# n=int(input("enter a number"))
# count=1
# for i in  range(1,n+1):
#         count=count*i

        
# print(f"factorina of {n} is ",{count})
# n=int(input("enter a numbr : "))
# for i in range (1,n+1):
#           print(" " *(n-i), end=" ")
#           print ("*"*(2*i-1),end=" ")
#           print ("")

n=int(input("Enter the number of :"))
for i in range(1,n+1):
          print("* "*i,end=" ")
          print("")

n=int(input("Enter the numjber : "))
for i in range (1,n+1):
          if(i==1 or i==n):
                print("*"*n,end="")
          else:
                print("*",end="")
                print(" "* (n-2),end="")
                print("*",end=" ")
          print(" ")
