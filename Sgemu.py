#Setting The Window.

import turtle,time,random # default in python
delay=0.1
sc=turtle.Screen()
sc.title("NagaRaja")
sc.bgcolor("Green")
sc.setup(width=600,height=600)
sc.tracer(0)    #mandatory

# Create Snake Head.

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("White")
head.goto(0,0)
head.penup()
head.direction="stop"

# Setting the Food in a random position.

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Orange")
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290))
# Score.
score=0
pencil=turtle.Turtle()
pencil.speed(0)
pencil.color("white")
pencil.penup()
pencil.goto(160,250)
pencil.shape("square")
pencil.write(f"SCORE:{score}",align='center',font=('courier',24,'bold'))
def up():
    if head.direction!="down":
        head.direction="up"
def down():
    if head.direction!="up":
        head.direction="down"
def right():
    if head.direction!="left":
        head.direction="right"
def left():
    if head.direction!="right":
        head.direction="left"
sc.listen()
sc.onkeypress(up,"Up")
sc.onkeypress(down,"Down")
sc.onkeypress(right,"Right")
sc.onkeypress(left,"Left")
body=[]
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
while True:
    sc.update()
    pencil.hideturtle()

    # Challenges.
    # Border Challenges.

    if head.xcor()>290 or head.ycor()>290 or head.xcor()<-290 or head.ycor()<-290:
        time.sleep(2)
        head.direction="stop"
        head.goto(0,0)
        for i in body:
            i.goto(1000,1000)
        body.clear()
        score=0
        #delay=0.1
        pencil.clear()
        pencil.write(f"SCORE:{score}",align='center',font=('courier',24,'bold'))

    # Snake Body Growth.

    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("Gray")
        new_body.penup()
        body.append(new_body)
        score+=1
        #delay-=0.01
        pencil.clear()
        pencil.write(f"SCORE:{score}",align='center',font=('courier',24,'bold'))
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()

    # Body Collision.

    for i in body:
        if i.distance(head)<20:
            time.sleep(2)
            head.direction="stop"
            head.goto(0,0)
            for i in body:
                i.goto(1000,1000)
            body.clear()
            score=0
            delay=0.1
            pencil.clear()
            pencil.write(f"SCORE:{score}",align='center',font=('courier',24,'bold'))
            
    time.sleep(delay) # Snake Moving time.






















sc.mainloop()   #mandatory
