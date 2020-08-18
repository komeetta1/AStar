import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1000,700)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Floor(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square") 
        self.color("blue")
        self.penup()
        self.speed(0) 

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")         
        self.color("yellow")           
        self.penup()                   
        self.speed(0) 

class GreenForward(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(90)
        self.shape("classic")
        self.color("green")
        self.penup()
        self.speed(0)

class GreenRight(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(0)
        self.shape("classic")
        self.color("green")
        self.penup()
        self.speed(0)

class GreenDown(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(270)
        self.shape("classic")
        self.color("green")
        self.penup()
        self.speed(0)

class GreenLeft(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(180)
        self.shape("classic")
        self.color("green")
        self.penup()
        self.speed(0)


class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

