"""
Made by Dhruv.

Program Briefing:
    1) This python program uses tkinter and pygame libraries to create animated graphs of a mathematical function.
    2) The mathematical function is defined in the `f(x, a)` function, which can be modified to change the graph.
    3) The Control Panel is created using tkinter, allowing users to adjust various parameters on the fly.
    4) The graph is drawn using pygame to allow real-time updates and animations.

Program Flow:
    1) Initialize pygame and tkinter.
    2) Create a window for the graph and a control panel.
    3) Define the mathematical function to be graphed.
    4) Set up controls for adjusting offsets and magnifications.
    5) Enter the main loop to update the graph and control panel in real-time.
    6) Handle user inputs to modify graph parameters dynamically.
"""


import pygame
from SETTINGS import *
import numpy
from math import sin, cos, tan, e, pi, pow, log10, log, sqrt
import time
import PointSet
from Control_Program import *
from Utility import *


pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock()

SetX = numpy.arange(0, 8, 0.01)
variable = 0
variable2 = 0
pointGroup = PointSet.PointGroup()

for i in range(len(SetX)):
    pointGroup.assign(PointSet.Point(PointSet.makePosition(i - 800, 0), i))

xOffset = 0
yOffset = 0
XMagnification = 1
YMagnification = 100

StringEquation = ""

Objects = []

control = Window(400, 250, "Control Panel")

Objects.append(control.add_text(15, 2, f"X-Offset : {xOffset}", 285, 0))
Objects.append(control.add_text(15, 2, f"Y-Offset : {yOffset}", 285, 40))
Objects.append(control.add_text(18, 2, f"X-Magnification : {XMagnification}", 265, 80))
Objects.append(control.add_text(18, 2, f"Y-Magnification : {YMagnification}", 265, 120))
Objects.append(control.add_button(4, 2, ">", 90, 45))  # Increase X offset
Objects.append(control.add_button(4, 2, "^", 50, 0))  # Increase Y offset
Objects.append(control.add_button(4, 2, "^", 150, 90))  # Increase X-Magnification
Objects.append(control.add_button(4, 2, "^", 150, 145))  # Increase Y-Magnification
Objects.append(control.add_button(4, 2, "<", 10, 45))  # Decrease X Offset
Objects.append(control.add_button(4, 2, "V", 50, 45))  # Decrease Y Offset
Objects.append(control.add_button(4, 2, "v", 190, 90))  # Decrease X-Magnification
Objects.append(control.add_button(4, 2, "v", 190, 145))  # Decrease Y-Magnification
Objects.append(control.add_button(15, 2, "RESET", 280, 200))

Objects.append(control.add_text(20, 2, "X-Magnification --> ", 0, 90))
Objects.append(control.add_text(20, 2, "Y-Magnification --> ", 0, 145))


# defines
def change_xOffset(event):
    global xOffset
    xOffset += event


def change_yOffset(event):
    global yOffset
    yOffset += event


def change_XMagnification(event):
    global XMagnification
    XMagnification += event


def change_YMagnification(event):
    global YMagnification
    YMagnification += event


def Reset():
    global XMagnification, YMagnification, xOffset, yOffset
    XMagnification = 1
    YMagnification = 100
    xOffset = 0
    yOffset = 0


Objects[4].bind("<Button-1>", lambda event: change_xOffset(1))
Objects[5].bind("<Button-1>", lambda event: change_yOffset(10))
Objects[6].bind("<Button-1>", lambda event: change_XMagnification(1))
Objects[7].bind("<Button-1>", lambda event: change_YMagnification(10))
Objects[8].bind("<Button-1>", lambda event: change_xOffset(-1))
Objects[9].bind("<Button-1>", lambda event: change_yOffset(-10))
Objects[10].bind("<Button-1>", lambda event: change_XMagnification(-1))
Objects[11].bind("<Button-1>", lambda event: change_YMagnification(-10))
Objects[12].bind("<Button-1>", lambda event: Reset())


def f(x, a=1):
    try:
        ans = sin((x * a) + a)
    except ZeroDivisionError:
        ans = 10000
    return ans


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            control.root.quit()
            exit(0)
    window.fill("white")
    pygame.display.set_caption(f"Animated Graph, FPS = {Clock.get_fps()}")

    for point in pointGroup.give():
        x = SetX[point.index] - WIDTH//200 + xOffset
        point.change_pos(PointSet.makePosition(point.originalX*XMagnification, f(x, variable)*YMagnification + yOffset))
        point.draw(window)

        if point.index != len(pointGroup.give()) - 1:
            pygame.draw.line(window, "black", point.pos, pointGroup.give()[point.index + 1].pos, 2)

    variable += 0.1

    Objects[0].config(text=f"X-Offset : {xOffset}")
    Objects[1].config(text=f"Y-Offset : {yOffset}")
    Objects[2].config(text=f"X-Magnification : {XMagnification}")
    Objects[3].config(text=f"Y-Magnification : {YMagnification}")

    pygame.display.flip()
    control.root.update()
    Clock.tick(FPS)
