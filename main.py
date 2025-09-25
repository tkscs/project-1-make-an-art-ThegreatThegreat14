import turtle

def big_shape(num_sides):
    for i in range(num_sides):
       turtle.forward(1000/num_sides)
       turtle.right(360/num_sides)

def small_shape(num_sides):
    for i in range(num_sides):
       turtle.forward(280/num_sides)
       turtle.right(360/num_sides)

turtle.left (90)
turtle.up()
turtle.forward (100)
turtle.down()
turtle.right (90)
big_shape (50)

turtle.up()
turtle.right (90)
turtle.forward (120)

turtle.right (90)
turtle.forward (30)
turtle.down()
turtle.left (90)
small_shape (100)
turtle.left (90)
turtle.up()
turtle.forward (60)
turtle.left (90)
turtle.down()
small_shape (100)
    

turtle.exitonclick()