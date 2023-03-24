import math
x1 = int(input("Co-Ordintes Of X1: "))
y1 = int(input("Co-Ordintes Of Y1: "))
x2 = int(input("Co-Ordintes Of X2: "))
y2 = int(input("Co-Ordintes Of Y2: "))
co_square = (x1-x2)**2 + (y1-y2)**2
result = round(math.sqrt(co_square),2)
print("Required Distance = ",result)