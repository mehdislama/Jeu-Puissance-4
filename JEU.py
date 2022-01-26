import turtle

wind=turtle.Screen()
wind.title("PING PONG BY Mahdouch")
wind.bgcolor("black")
wind.tracer(0)

"GAME LOOP"
raquet1= turtle.Turtle()
raquet1.speed(0)
raquet1.shape("square")
raquet1.color("blue")
raquet1.penup()
raquet1.shapesize(stretch_wid=5,stretch_len=0.5)
raquet1.goto(-350,0) #9adech yeb3ed 3al extremitè

raquet2= turtle.Turtle()
raquet2.speed(0)
raquet2.shape("square")
raquet2.color("blue")
raquet2.penup()
raquet2.shapesize(stretch_wid=5,stretch_len=0.5)
raquet2.goto(350,0) #9adech yeb3ed 3al extremitè


bal= turtle.Turtle() # initialisation mtaa objet
bal.speed(0)
bal.shape("circle") # nhotha mouraba3 wela dora...
bal.color("white")
bal.penup()
bal.goto(0,0) #9adech yeb3ed 3al extremitè
bal.dx=0.5
bal.dy=0.5




def raquet1_up():
    y=raquet1.ycor() # position mta objet al axe y
    y+=20
    raquet1.sety(y) # bech tekhou lposition jdida

wind.listen() #fama e7timel tenzel 3al clavier
wind.onkeypress(raquet1_up,"a") # ki nenzel 3al w khadem lfonction heki
def raquet1_down():
    y=raquet1.ycor() # position mta objet al axe y
    y-=20
    raquet1.sety(y) # bech tekhou lposition jdida

wind.listen() #fama e7timel tenzel 3al clavier
wind.onkeypress(raquet1_down,"q") # ki nenzel 3al w khadem lfonction heki

def raquet2_up():
    y=raquet2.ycor() # position mta objet al axe y
    y+=20
    raquet2.sety(y) # bech tekhou lposition jdida

wind.listen() #fama e7timel tenzel 3al clavier
wind.onkeypress(raquet2_up,"p") # ki nenzel 3al w khadem lfonction heki
def raquet2_down():
    y=raquet2.ycor() # position mta objet al axe y
    y-=20
    raquet2.sety(y) # bech tekhou lposition jdida

wind.listen() #fama e7timel tenzel 3al clavier
wind.onkeypress(raquet2_down,"m") # ki nenzel 3al w khadem lfonction heki

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.penup()
while True:
    wind.update()
    bal.setx(bal.xcor()+bal.dx)
    bal.sety(bal.ycor()+bal.dy)

    if bal.ycor()>249:
        bal.sety(249)
        bal.dy*=-1
    elif bal.ycor()<-249:
        bal.sety(-249)
        bal.dy*=-1
    if bal.xcor()>390:
        bal.setx(0)
        bal.dx*=-1
    if bal.xcor()<-390:
        bal.setx(0)
        bal.dx*=-1
        
