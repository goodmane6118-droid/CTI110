import turtle

t = turtle.Turtle()
t.pensize(4)
t.color("blue")
t.speed(5)

for i in range(4):
    t.forward(100)
    t.right(90)

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

t.penup()
t.forward(150)  
t.right(90)
t.forward(150)  
t.left(90)
t.pendown()

t.color("green")
t.pensize(6)

t.left(90)
t.forward(100)  

t.right(90)
for i in range(3):   
    t.forward(60)
    t.backward(60)
    if i < 2:
        t.right(90)
        t.forward(50)
        t.left(90)

t.penup()
t.left(90)
t.forward(100)  
t.right(90)
t.forward(120)  
t.pendown()

t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(180)

t.pendown()
t.forward(100)

t.hideturtle()
turtle.done()


