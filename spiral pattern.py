import turtle
my_wn = turtle.screen()
my_wn.bgcolor("light blue")
my_wn.title("turtle")
my_pen = turtle.turtle()
size = 0
while True:
    for i in range(4):
     my_pen.fd(size + 1) 
     my_pen.left(90)
     size = size - 5
    size = size + 1