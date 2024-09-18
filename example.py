
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
tip.goto(-30, -270) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 60, 130, "brown")# lebar dan tinggi pohon

# deklarasi puncak pohon
tip.penup()
tip.goto(-30, -270) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 200, 200, "green")# lebar dan tinggi pohon