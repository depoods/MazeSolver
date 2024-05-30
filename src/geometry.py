from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1x = point_1.x
        self.point_1y = point_1.y

        self.point_2x = point_2.x
        self.point_2y = point_2.y


    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1x, self.point_1y, self.point_2x, self.point_2y, fill=fill_color, width=2
            )
