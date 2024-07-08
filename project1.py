'''
1 for snale
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,-1])
youstr = input("enter your choice : ")
youdict ={"s":1,"w":-1,"g":0}
reversedict = {1:"snake",2:"water",3:"gun"}
you = youdict[youstr]
print(f"you choice {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer==you):
          print("its a draw")
else:
          if(you==1 and computer==-1):
                    print("you win")
          elif(you==0 and computer==-1):
                    print("you lose")
          elif(you==-1 and computer==1):
                    print("you lose")
          elif(you==0 and computer==1):
                    print("you win")
          elif(you==-1 and computer==0):
                              print("you win")
          elif(you==1 and computer==0):
                              print("you lose")
          else:
                  print("something went wrong! ")
