import turtle
import numpy as np
turtle.tracer (0,0)

shinysize = 1
# changes size of eye shinies and works well from around 0.3 to 1.25

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

for i in range (70):
    part_shape (1, 200)
turtle.right (180)
turtle.up()
for i in range (70):
    part_shape (1, -200)
turtle.right (180)
turtle.down()
for i in range (70):
    part_shape (1, -200)
turtle.right (180)
turtle.up()
for i in range (70):
    part_shape (1, 200)
turtle.right (180)
turtle.down()

# ears
turtle.up()
turtle.right (180)
turtle.forward (215)
turtle.left (90)

turtle.left (3)
for i in range (50):
    part_shape (20,-50)
for i in range (11):
    part_shape (20,-50)
turtle.down()

turtle.right (100)
for i in range (300, 600, 3):
    part_shape (1.5, i)
turtle.right (55)
for i in range (600, 320, -3):
    part_shape (1.5, i)

turtle.right (180)
turtle.up()
turtle.left (360/321)
for i in np.arange (-320, -600, -3):
    part_shape (1.5, i)
turtle.left (55)
for i in range (-600, -300, 3):
    part_shape (1.5, i)
turtle.right (360/600)
turtle.left (100)

turtle.right (8)
for i in range (22):
    part_shape (20,50)
turtle.down()

turtle.left (100)
for i in range (-300, -600, -3):
    part_shape (1.5, i)
turtle.left (55)
for i in range (-600, -320, 3):
    part_shape (1.5, i)

turtle.update()
turtle.exitonclick()