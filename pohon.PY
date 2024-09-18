
import turtle
import math

# deklarasi untuk menggambar persegi panjang
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


# deklarasi untuk menggambar segitiga
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

# deklarasi mengatur latar belakang
screen = turtle.Screen ( )
screen.bgcolor("blue")

# deklarasi turtle object
tip = turtle.Turtle ( )
tip.color ("white")
tip.shape ("turtle")
tip.speed (2)

# deklarasi dasar pohon
tip.penup()
tip.goto(100, -210)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
tip.penup()
tip.goto(100, -170)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
tip.penup()
tip.goto(100, -130)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")

# deklarasi puncank pohon
tip.penup()
tip.goto(65, -90)
tip.pendown()
drawTriangle(tip, 100, "yellow")
tip.penup()
tip.goto(70, -45)
tip.pendown()
drawTriangle(tip, 80, "red")
tip.penup()
tip.goto(75, -5)
tip.pendown()
drawTriangle(tip, 70, "brown")
tip.penup()
tip.goto(80, 30)
tip.pendown()
drawTriangle(tip, 60, "green")
tip.penup()
tip.goto(85, 60)
tip.pendown()
drawTriangle(tip, 50, "blue")
