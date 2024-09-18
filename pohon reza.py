
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
tip.goto(-30, -270) # MENGATUR POSISI BATANG POHON (-)kekiri (+)kekanan # mengatur posisi pohon keatas(+) kebawah(-)
tip.pendown()
drawRectangle(tip, 60, 130, "brown")# lebar dan tinggi pohon

# deklarasi puncak pohon
tip.penup()
tip.goto(-120, -140) # mengatur posisi segitiga - ke kiri + kekanan # mengatur posisi keatas (+) dan kebawah (-)
tip.pendown()
drawTriangle(tip, 250, "yellow") # besar segitiga dan warnannya

tip.penup()
tip.goto(-100, -40) # mengatur posisi segitiga - ke kiri + kekanan # mengatur posisi keatas (+) dan kebawah (-)
tip.pendown()
drawTriangle(tip, 200, "yellow") # besar segitiga dan warnannya

tip.penup()
tip.goto(-80, 40) # mengatur posisi segitiga - ke kiri + kekanan # mengatur posisi keatas (+) dan kebawah (-)
tip.pendown()
drawTriangle(tip, 150, "yellow") # besar segitiga dan warnannya

tip.penup()
tip.goto(-60, 100) # mengatur posisi segitiga - ke kiri + kekanan # mengatur posisi keatas (+) dan kebawah (-)
tip.pendown()
drawTriangle(tip, 100, "yellow") # besar segitiga dan warnannya

tip.penup()
tip.goto(-45, 140) # mengatur posisi segitiga - ke kiri + kekanan # mengatur posisi keatas (+) dan kebawah (-)
tip.pendown()
drawTriangle(tip, 70, "yellow") # besar segitiga dan warnannya