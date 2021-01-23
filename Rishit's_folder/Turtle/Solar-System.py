import turtle as t

# ----------------------------------------------
# creating the planets:
# inner planets:
overallSpeed =  10000

merc = t.Turtle()
merc.shape('circle')
merc.color('gray', 'gray')
merc.penup()
merc.shapesize(0.17)
merc.speed(overallSpeed)

mercAngle = 7.25
mercPos = 40

ven = t.Turtle()
ven.shape('circle')
ven.color('orange', 'orange')
ven.penup()
ven.shapesize(0.2)
ven.speed(overallSpeed)

venAngle = 3
venPos = 55

earth = t.Turtle()
earth.shape('circle')
earth.color('blue', 'blue')
earth.penup()
earth.shapesize(0.2)
earth.speed(overallSpeed)

earthAngle = 2.5
earthPos = 65

mars = t.Turtle()
mars.shape('circle')
mars.color('red', 'red')
mars.penup()
mars.shapesize(0.1)
mars.speed(overallSpeed)

marsAngle = 1
marsPos = 80

# outer planets:

jup = t.Turtle()
jup.shape('circle')
jup.color('tan', 'tan')
jup.penup()
jup.shapesize(1)
jup.speed(overallSpeed)

jupAngle = 0.2
jupPos = 140

sat = t.Turtle()
sat.shape('circle')
sat.color('#edd500', '#edd500')
sat.penup()
sat.shapesize(0.9)
sat.speed(overallSpeed)

satAngle = 0.15
satPos = 190

ur = t.Turtle()
ur.shape('circle')
ur.color('cyan', 'cyan')
ur.penup()
ur.shapesize(0.6)
ur.speed(overallSpeed)

urAngle = 0.06
urPos = 270

nep = t.Turtle()
nep.shape('circle')
nep.color('#000e8c', '#000e8c')
nep.penup()
nep.shapesize(0.55)
nep.speed(overallSpeed)

nepAngle = 0.017
nepPos = 315

# ----------------------------------------------


# ----------------------------------------------
# drawing the background:
radius = 21
t.speed(10000000)
t.color('yellow')
t.begin_fill()
t.getscreen()\
    .bgcolor('black')
t.goto(0, -radius)
t.pendown()
t.circle(radius)
t.penup()
t.hideturtle()
t.end_fill()
# ----------------------------------------------

# ----------------------------------------------
# move the planets:
merc.goto(0, mercPos)
merc.pendown()
ven.goto(0, venPos)
ven.pendown()
earth.goto(0, earthPos)
earth.pendown()
mars.goto(0, marsPos)
mars.pendown()
jup.goto(0, jupPos)
jup.pendown()
sat.goto(0, satPos)
sat.pendown()
ur.goto(0, urPos)
ur.pendown()
nep.goto(0, nepPos)
nep.pendown()
while True:
    merc.fd(5)
    merc.right(mercAngle)
    merc.fd(5)
    merc.right(mercAngle)

    ven.fd(3)
    ven.right(venAngle)
    ven.fd(3)
    ven.right(venAngle)

    earth.fd(3)
    earth.right(earthAngle)
    earth.fd(3)
    earth.right(earthAngle)

    mars.fd(1.5)
    mars.right(marsAngle)
    mars.fd(1.5)
    mars.right(marsAngle)

    jup.fd(0.5)
    jup.right(jupAngle)
    jup.fd(0.5)
    jup.right(jupAngle)

    sat.fd(0.5)
    sat.right(satAngle)
    sat.fd(0.5)
    sat.right(satAngle)

    ur.fd(0.3)
    ur.right(urAngle)
    ur.fd(0.3)
    ur.right(urAngle)

    nep.speed(1000000)
    nep.fd(0.1)
    nep.right(nepAngle)
    nep.fd(0.1)
    nep.right(nepAngle)
# ----------------------------------------------

t.done()