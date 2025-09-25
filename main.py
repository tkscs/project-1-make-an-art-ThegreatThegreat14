import turtle

def shape(size, num_sides):
    for i in range(num_sides):
       turtle.forward(size/num_sides)
       turtle.right(360/num_sides)

turtle.left (90)
turtle.up()
turtle.forward (100)
turtle.down()
turtle.right (90)
shape (1000,50)

turtle.up()
turtle.right (90)
turtle.forward (120)

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
    

turtle.exitonclick()