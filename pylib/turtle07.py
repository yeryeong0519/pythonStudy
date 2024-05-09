import turtle as t

def draw(x, y):
    t.setpos(x, y)
    
def move(x, y):
    t.up()
    t.setpos(x, y)
    t.down()
    
t.shape("turtle")
t.speed(0)
t.pensize(3)
t.onscreenclick(draw)
t.onscreenclick(draw)
t.onscreenclick(move, 3)
t.onkeypress(lambda : t.color("red"), "r")
t.onkeypress(lambda : t.color("green"), "g")
t.onkeypress(lambda : t.color("blue"), "b")
t.onkeypress(lambda : t.color("black"), "k")
t.onkeypress(lambda : t.pensize(1), "1")
t.onkeypress(lambda : t.pensize(3), "3")
t.onkeypress(lambda : t.pensize(5), "5")
t.listen
t.done()