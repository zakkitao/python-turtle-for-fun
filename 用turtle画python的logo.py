import turtle as t
t.getscreen().bgcolor("black")
t.setup(650,350,200,200)
t.pensize(15)
t.pencolor("yellow")
t.hideturtle()
t.speed(10)
#p
t.pu()
t.goto(-150,50)
t.pd()
t.seth(-90)
t.forward(110)
t.pu()
t.goto(-150,0)
t.seth(-30)
t.pd()
t.forward(15)
t.circle(25,120)
t.forward(30)
t.seth(110)
t.circle(25,120)

#y
t.pu()
t.goto(-70,55)
t.seth(-90)
t.pd()
t.forward(40)
t.circle(25,120)
t.pu()
t.goto(-25,55)
t.seth(-90)
t.pd()
t.fd(90)
t.seth(90)
t.circle(25,-40)
t.left(150)
t.forward(15)


#t
t.pencolor("white")
t.pu()
t.goto(10,70)
t.seth(-90)
t.pd()
t.fd(80)
t.circle(5,120)
t.pu()
t.goto(0,55)
t.seth(0)
t.pd()
t.forward(20)

#h
t.pu()
t.goto(45,80)
t.pd()
t.seth(-90)
t.forward(95)
t.pu()
t.goto(45,30)
t.pd()
t.circle(25,-150)
t.seth(-90)
t.fd(56)

#o
t.pu()
t.goto(145,-15)
t.seth(-180)
t.pd()
foot = 1.2
for a in range(2):
    for i in range(60):
        if i<30:
            foot += 0.03
            t.right(3)
            t.fd(foot)
        else:
            foot -= 0.03
            t.right(3)
            t.fd(foot)

#n
t.pu()
t.goto(200,55)
t.seth(-90)
t.pd()
t.forward(70)
t.goto(200,30)
t.circle(25,-150)
t.seth(-90)
t.fd(58)

#蟒蛇
t.pu()
t.goto(0,-20)
t.seth(-40)
t.pd()
t.pencolor("#082E54")
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)
t.circle(15,80)
t.circle(-15,80)

t.seth(0)
t.fd(15)
t.circle(10,180)
t.seth(-180)
t.fd(15)
t.pensize(1)
t.pencolor("black")
t.circle(1)
t.done()