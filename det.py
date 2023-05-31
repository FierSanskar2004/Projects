def det2b2(a,b,c,d):
  det=(a*d)-(b*c)
  print("Determinant = ",det)

def det3b3(a,b,c,d,e,f,g,h,i):
  det=a*(e*i-f*i)-b*(d*i-g*f)+c*(d*h-g*e)
  print("Determinant = ",det)

n=int(input("0 - 2 by 2 matrix \n 1- 3 by 3 matrix \n Choose one :"))

if n==0:
  a=int(input("a = "))
  b=int(input("b = "))
  c=int(input("c = "))
  d=int(input("d = "))
  print("Matrix")
  print("[",a," ",b,"]")
  print("[",c," ",d,"]")
  det2b2(a,b,c,d)
if n==1:
  a=int(input("a = "))
  b=int(input("b = "))
  c=int(input("c = "))
  d=int(input("d = "))
  e=int(input("e = "))
  f=int(input("f = "))
  g=int(input("g = "))
  h=int(input("h = "))
  i=int(input("i = "))
  print("Matrix")
  print("[",a," ",b," ",c,"]")
  print("[",d," ",e," ",f,"]")
  print("[",g," ",h," ",i,"]")
  det3b3(a,b,c,d,e,f,g,h,i)
else:
  print("Error! n given does not fall in binary.")