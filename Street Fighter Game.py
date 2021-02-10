import turtle

''' Ideas:

* = Favorite One

1) Street Fighter!  
  a) Animation(find animation package for turtle)
  b) Secrets powers(example: press i for player 1 and exctric shock)
  d) Make sure that AI does not use power srtike every time
  e) Optinal: AI can change characters
  f) Make a backgrond(Turtle Package(maybe random in future))
  g) seeing those effects(punches, specials powers, etc.) 
  h)  A way to check if how many hearts you have(a varible that ir connected to a turtle that draws and erases hearts)
  i) Packages
  j) Player v Player
  k) CPU
  l) Choose is Player v Player or CPU
  m) background music(and avatar music)
  
  Examples:
    import turtle
    import time
    
    screen = turtle.Screen()
    screen.setup(600,400)
    screen.bgpic('image1.gif')
    time.sleep(2)
    screen.bgpic('image2.gif')
    
    # click the image icon in the top right of the code window to see
    # which images are available in this trinket
    image = "rocketship.png"
    
    # add the shape first then set the turtle shape
    screen.addshape(image)
    turtle.shape(image)
    
    # Change images for animation
    
    
    Simplest Game:
      Player move around and have a special power(e.g. fireballs)
      
'''


# Our imports(libraries)
import turtle 
import time
import random
import pygame

# Music

pygame.mixer.init()

pygame.mixer.music.load("Ryu_music.mp3")
pygame.mixer.music.play(loops=0)


# Our Screen(With a battle background)

screen = turtle.Screen()
screen.setup(1280,540)
screen.bgpic("StreetFighterBg.gif")

# Players

# Player 1
Ryu = "Ryu.gif"
Player1 = turtle.Turtle()
screen.addshape(Ryu)
Player1.shape(Ryu)
print(Player1.shapesize())
Player1.penup()
Player1.speed(8000)
Player1.goto(400,-100)

# Player 2

Guile = "Guile.gif"
Player2 = turtle.Turtle()
screen.addshape(Guile)
Player2.shape(Guile)
print(Player1.shapesize())
Player2.penup()
Player2.speed(8000)
Player2.goto(-400,-100)

# 2 varibles: First for Guile and second for Ryu

# Heart varibles

Health_Bar1 = 100
Health_Bar2 = 100

# Health_Bar1

Health_Bar1_turtle = turtle.Turtle()
Health_Bar1_turtle.ht()
Health_Bar1_turtle.speed(0)
Health_Bar1_turtle.color("yellow")
Health_Bar1_turtle.penup()
Health_Bar1_turtle.goto(50,220)
Health_Bar1_turtle.pendown()


# Health_Bar2

Health_Bar2_turtle = turtle.Turtle()
Health_Bar2_turtle.ht()
Health_Bar2_turtle.speed(0)
Health_Bar2_turtle.color("yellow")
Health_Bar2_turtle.penup()
Health_Bar2_turtle.goto(-50,220)
Health_Bar2_turtle.left(180)
Health_Bar2_turtle.pendown()





# x value is 290 for the starting point. y value is 80.
Bg_Health_Bar = turtle.Turtle()
Bg_Health_Bar.color("#f01717")
Bg_Health_Bar.ht()
Bg_Health_Bar.speed(9000)
Bg_Health_Bar.penup()
Bg_Health_Bar.goto(-600,220)
Bg_Health_Bar.pendown()
Bg_Health_Bar.pensize(3)
Bg_Health_Bar.begin_fill()

for i in range(2):
    Bg_Health_Bar.forward(1200)
    Bg_Health_Bar.left(90)
    Bg_Health_Bar.forward(30)
    Bg_Health_Bar.left(90)
Bg_Health_Bar.end_fill()





# KO Bar

KO_Bar = turtle.Turtle()
KO_Bar.ht()
KO_Bar.speed(9000)
KO_Bar.penup()
KO_Bar.goto(-50,260)
KO_Bar.pendown()
KO_Bar.begin_fill()
for i in range(2):
    KO_Bar.forward(100)
    KO_Bar.right(90)
    KO_Bar.forward(60)
    KO_Bar.right(90)
KO_Bar.end_fill()
KO_Bar.color("white")
KO_Bar.penup()
KO_Bar.goto(-45,205)
KO_Bar.write("K.O", font=("Courier", 48, 'normal', 'bold', 'italic'))


# The names on the side

# Guile
Guile_name = turtle.Turtle()
Guile_name.ht()
Guile_name.speed(190000)
Guile_name.penup()
Guile_name.goto(-600,170)
Guile_name.color("#165307")
Guile_name.write("Guile", font=("Courier", 38, 'normal', 'bold', 'italic'))


# Ryu
Ryu_name = turtle.Turtle()
Ryu_name.ht()
Ryu_name.speed(190000)
Ryu_name.penup()
Ryu_name.goto(530,170)
Ryu_name.color("#dea116")
Ryu_name.write("Ryu", font=("Courier", 38, 'normal', 'bold', 'italic'))







# Functions fo moving and heart loss

# Heart loss when enemy attacks

# Ryu 
def drawHeart1():
    # If Ryu is dead
    if Health_Bar1 <= 0:
        Win_Player2 = turtle.Turtle()
        Win_Player2.ht()
        Win_Player2.speed(9000)
        Win_Player2.penup()
        Win_Player2.goto(-200,0)
        Win_Player2.color("#165307")
        Win_Player2.write("Guile Wins!", font=("Courier", 70, 'normal', 'bold', 'italic'))
        print("hi")
        Health_Bar1_turtle.clear()
    else:
        Health_Bar1_turtle.clear()
        # Health_Bar1_turtle
        size = 550 * Health_Bar1 / 100
        Health_Bar1_turtle.begin_fill()
        for i in range(2):
            Health_Bar1_turtle.forward(size)
            Health_Bar1_turtle.left(90)
            Health_Bar1_turtle.forward(30)
            Health_Bar1_turtle.left(90)
        Health_Bar1_turtle.end_fill()
    


# Guile

def drawHeart2():
    # If Ryu is dead
    if Health_Bar2 <= 0:
        Win_Player1 = turtle.Turtle()
        Win_Player1.ht()
        Win_Player1.speed(9000)
        Win_Player1.penup()
        Win_Player1.goto(-200,0)
        Win_Player1.color("#dea116")
        Win_Player1.write("Ryu Wins!", font=("Courier", 70, 'normal', 'bold', 'italic'))
        print("hi")
        Health_Bar2_turtle.clear()
    else:
        Health_Bar2_turtle.clear()
        # Health_Bar2_turtle
        size = 550 * Health_Bar2 / 100
        Health_Bar2_turtle.begin_fill()
        for i in range(2):
            Health_Bar2_turtle.forward(size)
            Health_Bar2_turtle.right(90)
            Health_Bar2_turtle.forward(30)
            Health_Bar2_turtle.right(90)
        Health_Bar2_turtle.end_fill()

# Movement function

def leftArrow():
    Player1.backward(30)

def Space():
    global Health_Bar2
    Ryu_punch = "Ryu_punch.gif"
    screen.addshape(Ryu_punch)
    Player1.shape(Ryu_punch)
    time.sleep(0.2)
    Ryu = "Ryu.gif"
    Player1.shape(Ryu)
    if Player1.distance(Player2) < 240:
        Health_Bar2 -= 5
        drawHeart2()
        Player2.backward(12)
    time.sleep(.1)
        
        
        
        
    
def rightArrow():
    Player1.forward(30)

def K():
    global Health_Bar2
    Ryu_kick = "Ryu_kick.gif"
    screen.addshape(Ryu_kick)
    Player1.shape(Ryu_kick)
    time.sleep(0.2)
    Ryu = "Ryu.gif"
    Player1.shape(Ryu)
    if Player1.distance(Player2) < 220:
        Health_Bar2 -= 10
        drawHeart2()
        Player2.backward(20)
    time.sleep(.1)
        


def P():
    global Health_Bar2
    Ryu_fight = "Ryu_fighting.gif"
    screen.addshape(Ryu_fight)
    Player1.shape(Ryu_fight)
    time.sleep(0.2)
    Ryu = "Ryu.gif"
    Player1.shape(Ryu)
    if Player1.distance(Player2) < 250:
        Health_Bar2 -= 15
        drawHeart2()
        Player2.backward(40)
    time.sleep(.1)

def upArrow():
    Ryu_Jump = "Ryu_Jump.gif"
    screen.addshape(Ryu_Jump)
    Player1.shape(Ryu_Jump)
    Player1.left(90)
    Player1.forward(200)
    Player1.left(180)
    time.sleep(0.5)
    Player1.forward(200)
    Player1.right(270)
    Ryu = "Ryu.gif"
    Player1.shape(Ryu)
    
    

screen.listen()
screen.onkey(leftArrow,"Left")
screen.onkey(Space,"space")
screen.onkey(rightArrow, "Right")
screen.onkey(K,"k")
screen.onkey(P,"p")
screen.onkey(upArrow,"Up",)



# Player 2

def A():
    Player2.backward(30)

    
def D():
    Player2.forward(30)

def Q():
    global Health_Bar1
    Guile_kick = "Guile_kick.gif"
    screen.addshape(Guile_kick)
    Player2.shape(Guile_kick)
    time.sleep(0.2)
    Guile = "Guile.gif"
    Player2.shape(Guile)
    if Player2.distance(Player1) < 235:
        Health_Bar1 -= 10
        drawHeart1()
        Player1.forward(20)
    time.sleep(.1)

def P2():
    global Health_Bar1
    Guile_Bam = "Guile-punch.gif"
    screen.addshape(Guile_Bam)
    Player2.shape(Guile_Bam)
    time.sleep(0.2)
    Guile = "Guile.gif"
    Player2.shape(Guile)
    if Player2.distance(Player1) < 235:
        Health_Bar1 -= 5
        drawHeart1()
        Player1.forward(12)
    time.sleep(.1)
def G():
    global Health_Bar1
    Guile_rkick = "Guile_flashkick.gif"
    screen.addshape(Guile_rkick)
    Player2.shape(Guile_rkick)
    time.sleep(0.2)
    Guile = "Guile.gif"
    Player2.shape(Guile)
    if Player2.distance(Player1) < 250:
        Health_Bar1 -= 15
        drawHeart1()
        Player1.forward(40)
    time.sleep(.1)

def W():
    Guile_Jump = "Guile_jump.gif"
    screen.addshape(Guile_Jump)
    Player2.shape(Guile_Jump)
    Player2.left(90)
    Player2.forward(200)
    Player2.left(180)
    time.sleep(0.5)
    Player2.forward(200)
    Player2.right(270)
    Guile = "Guile.gif"
    Player2.shape(Guile)
    

screen.listen()
screen.onkey(leftArrow,"Left")
screen.onkey(Space,"space")
screen.onkey(rightArrow, "Right")
screen.onkey(K,"k")
screen.onkey(P,"p")
screen.onkey(upArrow,"Up",)
screen.onkey(A,"a")
screen.onkey(D,"d")
screen.onkey(Q,"q")
screen.onkey(P2,"e")
screen.onkey(G,"g")
screen.onkey(W,"w")







drawHeart1()
drawHeart2()





