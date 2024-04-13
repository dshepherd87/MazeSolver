from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def get_canvas(self):
        return self.__canvas

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

class Line:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def draw(self, canvas, fill_color="black"):
        x1 = self.__a.get_x()
        y1 = self.__a.get_y()
        x2 = self.__b.get_x()
        y2 = self.__b.get_y()
        canvas.create_line(x1,y1,x2,y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, x1, y1, x2, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        canvas = self._win.get_canvas()
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_wall.draw(canvas)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            right_wall.draw(canvas)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x2,self._y2),Point(self._x1, self._y2))
            bottom_wall.draw(canvas)
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
            left_wall.draw(canvas)