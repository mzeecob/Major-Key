from aluLib import *
window_height = 500
window_width = 500
# Parameters that contain an x represent x coordinates, and y represent y coordinates
# Parameters with a 1 define the first line, parameters with a 2 define the second
# x1a and y1a define 1 point together, same for x2a and y2a etc.

def draw_line_art(x1a, y1a, x1b, y1b, x2a, y2a, x2b, y2b, line_count):
    count = 1
    while count <= line_count:
        set_stroke_color(1, 0, 0)
        draw_line(x1a, y1a, x1b, y1b)   # first base line on top
        draw_line(x2a, y2a, x2b, y2b)   # second base line on bottom
        draw_line(x1a, y1a, x2b, y2b)   # first intermediate line
        draw_line(x1a + (count/line_count)*(x1b - x1a), y1a + (count/line_count)*(y1b - y1a), x2b - (count/line_count)*(x2b - x2a), y2b - (count/line_count)*(y2b - y2a))
        count += 1



def main():
    # Start some line art, the first 4 parameters represent the coordinates of 2 points, which define a line
    # The next 4 coordinates also represent 2 points, which define a second line
    # The final parameter represents how many partial lines are desired
    set_fill_color(0, 0, 0)
    draw_rectangle(0, 0, window_height, window_width)
    draw_line_art(80, 90, 400, 50, 100, 300, 420, 350, 5)

start_graphics(main, height=window_height, width=window_width)