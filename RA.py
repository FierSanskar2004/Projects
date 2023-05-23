#This is a code for regression analysis
import math
x=list()
y=list()
n=int(input("Enter the number of data :"))

print(" Values of x :\n")
for i in range(0, n):
    ele = float(input("Read the x value :"))
    x.append(ele)

print(" Values of y :\n")
for j in range(0, n):
    lel = float(input("Read the y value :"))
    y.append(lel)
    
print("\nx : ",x)
print("y : ",y)

sumx=0
for i in range(0,n):
    sumx=sumx+x[i]
    
sumy=0
for j in range(0,n):
    sumy=sumy+y[j]

x_b=sumx/n
y_b=sumy/n

print("\nAverages:")
print("avg of x = ",x_b)
print("avg of y = ",y_b,"\n")

xdev=list()
ydev=list()
bah=0
puh=0

for i in range(0,n):
   bah=x[i]-x_b
   xdev.append(bah)

for j in range(0,n):
   puh=y[j]-y_b
   ydev.append(puh)
   
sxx=0
syy=0
for du in xdev:
  sxx=sxx+(du*du)

for da in ydev:
  syy=syy+(da*da)


sxy=0
wah=0
for ai, um in zip(xdev, ydev):
    wah = ai * um
    sxy += wah 

print("sxx = ",sxx)
print("syy = ",syy)
print("sxy = ",sxy)

cn=sxy/math.sqrt(sxx*syy)

if cn>-1 and cn<1:
  print("Relation between x and y is present.")
else:
  print("No relation is possible.")

if cn>-1 and cn<1:
  alp=y_b-(sxy/sxx)*x_b
  bet=(y_b*n-n*alp)/(x_b*n)
  if bet>=0:
    print("Equation : y = ",alp," + ",bet,"x")
  else:
    print("Equation : y = ",alp,bet,"x")
else:
  print("Error!")