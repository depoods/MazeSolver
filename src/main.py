from window import Window
from geometry import Line, Point

def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(20, 20)
    line_1 = Line(point1, point2)
    win.draw_line(line_1, "red")
    win.wait_for_close()



main()
