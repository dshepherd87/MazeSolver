from graphics import Window, Point, Line, Cell

def main():
    win = Window(1000, 1000)
    cell_1 = Cell(100, 100, 200, 200, win)
    cell_1.draw()
    cell_2 = Cell(100, 200, 200, 300, win, right_wall=False)
    cell_2.draw()
    cell_3 = Cell(200, 200, 300, 300, win, left_wall = False)
    cell_3.draw()
    win.wait_for_close()

main()