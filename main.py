import turtle
import numpy as np
turtle.tracer (0,0)

def shape(size, num_sides):
    for i in range(num_sides):
       turtle.forward(size/num_sides)
       turtle.right(360/num_sides)

def semi(size, num_sides):
    for i in range(num_sides):
       turtle.forward(size/num_sides)
       turtle.right(90/num_sides)


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
turtle.left (90)
semi (40, 50)
def part_shape(num_sides):
    turtle.forward(1)
    turtle.right(360/num_sides)
for i in range(180, 400, 5):
    part_shape(i)
    
turtle.update()

turtle.exitonclick()