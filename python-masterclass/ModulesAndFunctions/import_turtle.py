# import turtle
#
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()
# import turtle
from turtle import *
# import math
from math import radians, cos
from time import sleep


def square(length: int) -> None:
    """Draws a square of length `length"""
    inner_forward = forward
    inner_right = right
    for side in range(4):
        inner_forward(length)
        inner_right(90)


def encircle_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle
"""
    square(length)
    # angle = math.radians(45)
    angle = radians(45)
    # radius = length * math.cos(angle)
    radius = length * cos(angle)
    right(135)
    circle(radius)
    left(135)
    print(f'Inside function, namespace is: {dir()}')
    print(f'locals: {locals()}')



# encircle_square(100)
speed('fast')
Screen().tracer(0)  # disable turtle animation

for s in range(72):
    # square(120)
    encircle_square(120)
    left(5)
    sleep(0.01)
    Screen().update()

Screen().update()   # update the screen
done()

# print(f'Main locals: {locals()}')
print(dir())
g = globals()
print(g['square'])

print(dir(__builtins__))
