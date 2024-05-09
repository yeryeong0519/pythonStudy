import turtle as t

def draw(head, dist):
    t.setheading(head)
    t.forward(dist)
    
    
def toleft():
    draw(180, 15)
    
def toright():
    draw(0, 15)
    
def toup():
    draw(90, 15)
    
def todown():
    draw(270, 15)
    
def move(x, y):
    t.up()
    t.setpos(x, y)  #거북이의 좌표를 옮긴다.
    t.down()
    
def red():
    t.pencolor("red")

def black():
    t.pencolor("black")
    
def thick():
    t.pensize(5)

def thin():
    t.pensize(1)
    
    
    
t.shape("turtle")
t.speed(0)
t.onkeypress(toleft, "Left")
t.onkeypress(toright, "Right")
t.onkeypress(todown, "Down")
t.onkeypress(toup, "Up")
t.onkeypress(red, "r")
t.onkeypress(black, "b")
t.onkeypress(thick, "5")
t.onkeypress(thin, "1")
t.onscreenclick(move)
t.listen()
t.done()