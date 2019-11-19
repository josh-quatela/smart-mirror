from graphics import *
win = GraphWin()
import turtle

f = open('weather','w')

#pt = (100,50)
#cir = Circle(pt, 25)
#cir.draw(win)

#cir.setOutline('red')
#cir.setFill('blue')

message = """<html>
<head></head>
<body><p>
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
</p></body>
</html>
"""

f.write(message)
f.close()
