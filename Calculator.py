a=int(input("a = "))
b=int(input("b = "))
response=str(input("What do you want to do?\n"))

if(response=="Addition" or response=="addition"):
  print("a + b = ",a+b)
elif(response=="Subtraction" or response=="subtraction"):
  print("a - b = ",a-b) 
elif(response=="Multipication" or response=="multipication"):
  print("a * b = ",a*b)
elif(response=="Division" or response=="division"):
  print("a / b = ",a/b)
elif(response=="Modulus" or response=="modulus"):
  print("a % b = ",a%b)
elif(response=="Floor division" or response=="floor division"):
  print("a + b = ",a+b)
else:
    print("Error! Operator not in the specified list.")