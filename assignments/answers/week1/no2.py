# Rectangle 1
x1 = float(input("Enter the x coordinate of Rectangle 1: "))
y1 = float(input("Enter the y coordinate of Rectangle 1: "))

while True:
    rectangle1_width = float(input("Enter the width of Rectangle 1: "))
    rectangle1_height = float(input("Enter the height of Rectangle 1: "))
    if rectangle1_width > 0 and rectangle1_height > 0:
        break
    else:
        print("Width and height must be positive numbers. Please try again.")

# Rectangle 2
x2 = float(input("Enter the x coordinate of Rectangle 2: "))
y2 = float(input("Enter the y coordinate of Rectangle 2: "))

while True:
    rectangle2_width = float(input("Enter the width of Rectangle 2: "))
    rectangle2_height = float(input("Enter the height of Rectangle 2: "))
    if rectangle2_width > 0 and rectangle2_height > 0:
        break
    else:
        print("Width and height must be positive numbers. Please try again.")

# finding edges
def rectangle_edges(x, y, width, height):
    left = x - width / 2
    right = x + width / 2
    top = y + height / 2
    bottom = y - height / 2
    return left, right, top, bottom

left1, right1, top1, bottom1 = rectangle_edges(x1, y1, rectangle1_width, rectangle1_height)
left2, right2, top2, bottom2 = rectangle_edges(x2, y2, rectangle2_width, rectangle2_height)

if left1 >= left2 and right1 <= right2 and top1 <= top2 and bottom1 >= bottom2:
    print("Rectangle 1 is inside Rectangle 2")
elif left2 >= left1 and right2 <= right1 and top2 <= top1 and bottom2 >= bottom1:
    print("Rectangle 2 is inside Rectangle 1")
else:
    print("The rectangles do not contain each other")

# Check overlap
if right1 < left2 or left1 > right2 or top1 < bottom2 or bottom1 > top2:
    print("The rectangles do not overlap.")
else:
    print("The rectangles overlap.")

# print(rectangle_edges(x1,y1,rectangle1_width,rectangle1_height))
# print(rectangle_edges(x2,y2,rectangle2_width,rectangle2_height))
