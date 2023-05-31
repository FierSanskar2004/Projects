def fac(n):
  fac=1
  i=1
  if n==1 or n==0:
    return 1
  elif n>1:
    for i in range(1,n+1):
      fac=fac*i
  return fac

def ncr(n,r):
  if n>r:
    ncr=fac(n)/(fac(r)*fac(n-r))
    return ncr
  else:
    return "Math Error!"

a=float(input("a = "))
b=float(input("b = "))
response=str(input("What do you want to do?\n"))

if(response=="addition" or response=="add"):
    print("a + b = ",a+b)
elif(response=="subtraction" or response=="subtract"):
    print("a - b = ",a-b) 
elif(response=="multipication" or response=="multiply"):
    print("a * b = ",a*b)
elif(response=="division" or response=="divide"):
    print("a / b = ",a/b)
elif(response=="Modulus" or response=="modulus"):
    print("a % b = ",a%b)
elif response=="Exponention" or response=="exponention":
    print("a^b = ",a**b)
elif(response=="Floor division" or response=="floor"):
    print("a // b = ",a//b)
elif(response=="Factorial"):
  print(a,"! = ",fac(a))
  print(b,"! = ",fac(b))
elif(response=="ncr" or response=="Combination"):
  print(a,"c",b," = ",ncr(a,b))
else:
    print("Error! Operator not in the specified list.")
