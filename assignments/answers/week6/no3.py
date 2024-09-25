import tkinter as tk

class CircleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Drawer")
        
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.draw_circle)  
        self.canvas.bind("<Button-3>", self.remove_circle)

    def draw_circle(self, event):
        radius = 20
        x, y = event.x, event.y
        circle = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black")
        self.canvas.tag_bind(circle, "<Button-3>", lambda event, c=circle: self.remove_circle(event, c))

    def remove_circle(self, event, circle=None):
        if circle is None:
            x, y = event.x, event.y
            items = self.canvas.find_overlapping(x - 1, y - 1, x + 1, y + 1)
            for item in items:
                if self.canvas.type(item) == "oval":
                    self.canvas.delete(item)
        else:
            self.canvas.delete(circle)

def main():
    root = tk.Tk()
    circle_drawer = CircleDrawer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
