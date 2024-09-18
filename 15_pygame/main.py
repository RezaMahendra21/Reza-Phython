import pygame as pg

# init
pg.init()

# membuat display surface object
window_panjang = 500
window_lebar = 500
window = pg.display.set_mode((window_lebar, window_panjang))

# variable running game
isRun = True

# object game
# 1 posisi
x = 250
y = 250
# 2 ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10


while isRun :
    pg.time.delay(8)

    # user input, database input
    for ev in pg.event.get() :
        if ev.type == pg.QUIT :
            isRun = False

    # mengambil aksi dalam keyboard
    key = pg.key.get_pressed()

    # aksi gerak
    if key[pg.K_LEFT] and x > 0 : #agar object tidak keluar
        x-=speed
    if key[pg.K_RIGHT] and x < window.get_width() - lebar :
        x+=speed
    if key[pg.K_UP] and y > 0 :
        y -= speed
    if key[pg.K_DOWN] and y < window.get_height() - panjang :
        y+=speed

    # update asset
    window.fill((255,255,255)) # background warna putih
    pg.draw.rect(window, (255,120,41), (x,y,lebar,panjang))



    # render ke display
    pg.display.update()

pg.quit()