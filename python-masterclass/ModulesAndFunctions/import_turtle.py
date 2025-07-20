# import turtle
#
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

import turtle
# import math
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length"""
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


def encircle_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle
"""
    square(length)
    # angle = math.radians(45)
    angle = radians(45)
    # radius = length * math.cos(angle)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)
    print(f'Inside function, namespace is: {dir()}')
    print(f'locals: {locals()}')



# encircle_square(100)
# turtle.speed('fast')
# for s in range(72):
#     # square(120)
#     encircle_square(120)
#     turtle.left(5)
#
# turtle.done()

# print(f'Main locals: {locals()}')
print(dir())
g = globals()
print(g['square'])

print(dir(__builtins__))
