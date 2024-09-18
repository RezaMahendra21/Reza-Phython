
import turtle
import math

# deklarasi untuk menggambar persegi panjang 1
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

# deklarasi untuk menggambar persegi panjang 2
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


# deklarasi untuk menggambar persegi empat atas
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
# deklarasi untuk menggambar persegi empat atas 2
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
tip.speed (5)

# deklarasi dasar pohon 1
tip.penup()
tip.goto(-20, -270) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 25, 50, "black")# lebar dan tinggi pohon

tip.penup()
tip.goto(-20, -220) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 25, 50, "brown")# lebar dan tinggi pohon

# deklarasi puncak pohon
tip.penup()
tip.goto(-80, -170) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 150, 100, "black")# lebar dan tinggi pohon

tip.penup()
tip.goto(-80, -70) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 150, 100, "green")# lebar dan tinggi pohon

tip.penup()
tip.goto(-80, 30) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 150, 100, "red")# lebar dan tinggi pohon


# deklarasi dasar pohon 2
tip.penup()
tip.goto(200, -270) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 25, 50, "brown")# lebar dan tinggi pohon
tip.penup()
tip.goto(200, -220) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 25, 50, "black")# lebar dan tinggi pohon

# deklarasi puncak pohon
tip.penup()
tip.goto(150, -170) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 150, 100, "black")# lebar dan tinggi pohon

tip.penup()
tip.goto(150, -70) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 150, 100, "green")# lebar dan tinggi pohon
