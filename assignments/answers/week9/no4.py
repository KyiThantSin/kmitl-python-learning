class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle2D:
    def __init__(self, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

    def __str__(self):
        return f"The bounding rectangle is centered at ({self.center_x}, {self.center_y}) with width {self.width} and height {self.height}"

def getRectangle(points):
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]
    
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    
    return Rectangle2D(center_x, center_y, width, height)

def main():
    input_data = input("Enter the points: ")
    
    coordinates = list(map(float, input_data.split()))
    
    points = [Point(coordinates[i], coordinates[i + 1]) for i in range(0, len(coordinates), 2)]
    
    bounding_rectangle = getRectangle(points)
    
    print(bounding_rectangle)

if __name__ == "__main__":
    main()
