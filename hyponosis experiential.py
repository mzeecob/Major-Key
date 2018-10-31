from aluLib import *
rectangle_width = 1000
rectangle_height = 600
count = 0
def hypo1():
    set_fill_color(1,0,0)
    draw_circle(450,350,100)
    set_fill_color(0,1,0)
    draw_circle(450,350,60)
    set_fill_color(0,0,1)
    draw_circle(450,350,30)

def hypo2():
    set_fill_color(0,0,1)
    draw_circle(450,350,100)
    set_fill_color(0,0,1)
    draw_circle(450,350,60)
    set_fill_color(1,0,0)
    draw_circle(450,350,30)

def hypo3():
    set_fill_color(0,0,1)
    draw_circle(450,350,100)
    set_fill_color(0,1,0)
    draw_circle(450,350,60)
    set_fill_color(0,1,0)
    draw_circle(450,350,30)
def hypo4():
    global count
    if count % 3 == 0:
        hypo1()
    if count % 3 == 1:
        hypo2()
    else:
        hypo3()
    count += 1
start_graphics(hypo4, framerate = 8, width=rectangle_width, height=rectangle_height)


