# # name = "ravilumar"
# # print(len(name))
# # namesort =name[2:9]
# # print (namesort)
# # character1=name[1]
# # print(character1) #output is "a" b/c  at first position digit is "a" in ravikumar


# # negative concept in python
name = "ravilumar"
print(name[-8:-1]) #output is "r" b/c  at last position digit is "
# r    a     v    i    k   u    m   a    r
-9   -8  -7  -6  -5   -4   -3  -2  -1
print (name[1:8]) #output is
print(name[1:8:2])
print (name.endswith("uma"))
print (name.startswith("ra"))
print(name.capitalize())
print(name.upper())



# # escape_seq function in python 
a="ravi is a good  boy\nbut not a bed boy "
print(a)

#practic of chapter 3
#question 1;
name = input()
print(f"good Afternoon ,{name}")
#question 2;
letter =  '''Dear <|name|>, 
You are selected 
<|data|>'''
print(letter.replace("<|name|>","RAVI").replace("<|data|>","02-08-2000"))
#question 3;
name = "Ravi kumar is a  good  boy and "
print(name.find("Ravi"))
print(name.replace("  "," "))