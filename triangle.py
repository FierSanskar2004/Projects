import math


def dtct(l, m, n):
  exp = ((l * l) + (m * m) - (n * n)) / (2 * l * m)
  angle = math.acos(exp)
  angle = angle * 57.2957795131
  print("∟ = ", angle)


x1 = int(input("x = "))
y1 = int(input("y = "))
A = (x1, y1)
print("A = ", A)
x2 = int(input("x = "))
y2 = int(input("y = "))
B = (x2, y2)
print("B = ", B)
x3 = int(input("x = "))
y3 = int(input("y = "))
C = (x3, y3)
print("C = ", C)
SA = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
print("AB = ", SA)
SB = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
print("BC = ", SB)
SC = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
print("CA = ", SC)
P = SA + SB + SC
S = P / 2
print("Perimeter = ", P)
print("Semiperimeter = ", S)

test = 100

if P - SA > SA and P - SB > SB and P - SC > SC:
  print("The triangle is existent.")
  test = 1
else:
  print("The triangle is non-existent.")
  test = 0

if test == 1:
  AA = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
  print("The area is ", AA)
else:
  print("Cannot find area of the invalid triangle.")

mi = 0
if test == 1:
  dtct(SA, SB, SC)
  dtct(SB, SC, SA)
  dtct(SC, SA, SB)
else:
  print("Cannot find angles of the invalid triangle.")
