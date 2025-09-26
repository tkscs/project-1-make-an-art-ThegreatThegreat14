import turtle
import numpy as np

def shape(size, num_sides):
    for i in range(num_sides):
       turtle.forward(size/num_sides)
       turtle.right(360/num_sides)

# head
turtle.left (90)
turtle.up()
turtle.forward (100)
turtle.down()
turtle.right (90)
shape (1000,50)
turtle.right (36/50)
turtle.forward (10)

turtle.up()
turtle.right (90)
turtle.forward (120)

# eyes
turtle.right (90)
turtle.forward (30)
turtle.down()
turtle.left (90)
shape (280,100)
turtle.left (90)
turtle.up()
turtle.forward (60)
turtle.left (90)
turtle.down()
shape (280,100)

# nose
turtle.left (90)
turtle.up()
turtle.forward (30)
turtle.left (90)
turtle.forward (35)
turtle.down()
def part_shape(num_sides):
    turtle.forward(3)
    turtle.right(360/num_sides)
for i in range(180, 200, 10):
    part_shape(i)
    

turtle.exitonclick()