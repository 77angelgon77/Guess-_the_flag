import turtle
s = turtle.Screen()
s.bgcolor("grey")
t = turtle.Turtle()


def france():
    t.pu()
    t.goto(-200,50)
    t.pd()
    t.fillcolor("blue")
    
    t.pencolor("blue")
    t.begin_fill()
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.end_fill()
    
    t.rt(90)
    t.fd(200)
    
    t.fillcolor("white")
    
    t.pencolor("white")
    t.begin_fill()
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.end_fill()
    
    t.rt(90)
    t.fd(200)
    
    t.fillcolor("red")
    
    t.pencolor("red")
    t.begin_fill()
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(400)
    t.end_fill()
    
    t.pu()
    t.fd(10000)

def japan():
    t.pd()
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.fd(100)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(500)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(500)
    t.end_fill()
    t.bk(155)
    t.lt(90)
    t.fd(150)
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    r = 100
    t.circle(r)
    t.end_fill()

def saudiArabia():

    t.pd()
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    t.fd(100)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(500)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(500)
    t.end_fill()
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.pencolor("white")
    t.fd(300)
    t.pu()
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.pd()
    
    t.write("لَا إِلٰهَ إِلَّا الله مُحَمَّدٌ رَسُولُ الله", move = True , font=("Arial", 30, "bold"))


def latvia():
    t.fillcolor("red")
    
    t.begin_fill()
    
    for i in range(2):
        t.fd(300)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    
    t.rt(90)
    t.fd(100)
    t.begin_fill()
    t.fillcolor("white")
    
    for i in range(2):
        t.fd(100)
        t.lt(90)
        t.fd(300)
        t.lt(90)
    t.end_fill()
    
    
    t.fd(200)
    t.lt(90)
    t.begin_fill()
    t.fillcolor("red")
    
    for i in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(100)
        t.lt(90)
    t.end_fill()
def italy():
    t.fillcolor("green")
    
    t.begin_fill()
    
    for i in range(2):
        t.fd(100)
        t.rt(90)
        t.fd(200)
        t.rt(90)
    t.end_fill()
    t.fd(100)
    t.begin_fill()
    t.fillcolor("white")
    
    for i in range(2):
        t.fd(100)
        t.rt(90)
        t.fd(200)
        t.rt(90)
    t.end_fill()
    t.fd(100)
    t.begin_fill()
    t.fillcolor("red")
    
    for i in range(2):
        t.fd(100)
        t.rt(90)
        t.fd(200)
        t.rt(90)
    t.end_fill()
def sweeden():
    t.pencolor("white")
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(300)
        t.rt(90)
        t.fd(160)
        t.rt(90)
    t.end_fill()
    t.fillcolor("yellow")
    t.fd(100)
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(160)
        t.rt(90)
        t.fd(30)
    t.end_fill()
    t.fd(200)
    t.rt(90)
    t.fd(70)
    t.rt(90)
    t.begin_fill()
    for i in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()


def poland():
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.fillcolor("red")
    t.lt(90)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.rt(90)
        t.fd(200)
        t.rt(90)
    t.end_fill()


def nigeria():
    s.bgcolor("green")

    t.pu()
    t.pencolor("white")
    t.goto(145,500)
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(1000)
        t.rt(90)
        t.fd(290)
    t.end_fill()




def ireland():
    s.bgcolor("green")
    t.pu()
    t.pencolor("white")
    t.goto(145,500)
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(1000)
        t.rt(90)
        t.fd(290)
    t.end_fill()
    
    t.pu()
    t.pencolor("orange")
    t.goto(-146,500)
    t.pd()
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(1000)
        t.rt(90)
        t.fd(390)
    t.end_fill()

def switzerland():
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.pd()
    t.fd(200)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(200)
    t.end_fill()
    
    t.pu()
    t.goto(70,-20)
    t.pencolor("white")
    t.fillcolor("white")
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.pd()
    
    t.begin_fill()
    for i in range (2):
        t.fillcolor("white")
    
    
        t.fd(20)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(140,-90)
    t.rt(90)
    
    t.pd()
    t.begin_fill()
    for i in range (2):
        t.fillcolor("white")
    
    
        t.fd(20)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()


def israel():

    t.fillcolor("blue")

    t.pu()
    t.goto(-160,-250)
    t.pendown()

    t.lt(90)

    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(200)
        t.rt(90)
        t.fd(50)
    t.end_fill()

    t.penup()
    t.fd(180)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(200)
        t.rt(90)
        t.fd(50)
    t.end_fill()

    t.penup()
    t.bk(100)
    t.rt(90)
    t.fd(75)
    t.pendown()

    for i in range(3):
        t.fd(50)
        t.rt(120)

    t.penup()
    t.fd(20)
    t.rt(120)
    t.bk(10)
    t.pendown()

    for i in range(3):
        t.fd(50)
        t.lt(120)

nigeria()
flags=[france, japan , saudiArabia , latvia , switzerland ,italy, sweeden, israel, nigeria, ireland, poland]

turtle.done()