# point 0
x0 = float(input("Enter x coordinate of p0: "))
y0 = float(input("Enter y coordinate of p0: "))

#point 1
x1 = float(input("Enter x coordinate of p1: "))
y1 = float(input("Enter y coordinate of p1: "))

#point 2
x2 = float(input("Enter x coordinate of p2: "))
y2 = float(input("Enter y coordinate of p2: "))

cross_product = (x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0)

if cross_product > 0:
    print("The point p0 is on the left side of p1 and p2")
elif cross_product < 0:
    print("The point p0 is on the right side of p1 and p2")
else:
    print("The point p0 is on the line between p1 and p2")
