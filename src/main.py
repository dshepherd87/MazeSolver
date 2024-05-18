from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(500, 500)
    maze = Maze(250, 250, 30, 20, 20, 20, win, 125)
    maze.solve()
    win.wait_for_close()

main()