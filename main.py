import turtle
import numpy as np
turtle.tracer (0,0)

shinysize = 1

def shape(size, num_sides):
    for i in range(num_sides):
       turtle.forward(size/num_sides)
       turtle.right(360/num_sides)

def part_shape(size, num_sides):
    turtle.forward(size)
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

# left eye
turtle.right (90)
turtle.forward (30)
turtle.down()
turtle.left (90)
shape (280,100)

# left shinies
turtle.up()
turtle.right (180)
for i in range(9):
    part_shape (2.8,-100)
turtle.left (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(100):
    part_shape (shinysize,-100)
for i in range(50):
    part_shape (shinysize,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(100):
    part_shape (2*shinysize/3,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(50):
    part_shape (shinysize,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.right (90)
for i in range(9):
    part_shape (2.8,100)
turtle.down()

# right eye
turtle.left (90)
turtle.up()
turtle.forward (60)
turtle.left (90)
turtle.down()
shape (280,100)

# right shinies
for i in range (50):
    part_shape (2.8,100)
turtle.up()
turtle.right (180)
for i in range(9):
    part_shape (2.8,-100)
turtle.left (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(100):
    part_shape (shinysize,-100)
for i in range(50):
    part_shape (shinysize,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(100):
    part_shape (2*shinysize/3,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.down()
turtle.right (90)
for i in range(50):
    part_shape (shinysize,-100)
turtle.up()
turtle.right (90)
turtle.forward (10)
turtle.right (90)
for i in range(9):
    part_shape (2.8,100)
for i in range (50):
    part_shape (2.8,100)
turtle.down()

# nose
turtle.left (90)
turtle.up()
turtle.forward (30)
turtle.left (90)
turtle.forward (35)
turtle.down()
turtle.left (90)
for i in range(200, 280, 2):
    part_shape(1,i)
turtle.right (29)
for i in range(180, 450, 5):
    part_shape(1,i)
turtle.right (45)
for i in range(450, 180, -5):
    part_shape(1,i)
turtle.right (29)
for i in range(200, 280, 2):
    part_shape(1,i)
turtle.forward (1)
turtle.right (360/282)
turtle.forward (1)
turtle.right (360/284)

# mouth
turtle.up()
turtle.right (90)
turtle.forward (60)
turtle.down()


    
turtle.update()
turtle.exitonclick()