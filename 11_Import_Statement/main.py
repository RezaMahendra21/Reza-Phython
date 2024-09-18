import time

import os as cm
import andrian
# from aritmatika import tambah
from aritmatika import *

# Import Naruto
# import anime.naruto as naruto
# import naruto dengan __init__
import anime

# import fisika.testSaja as fs
import fisika
# impor fisika dengan init

tStart = time.time()

cm.system('clear')

andrian.loveMe("Akuu")
print(andrian.love("Diaaaa"))

print(kali(3,5,7,6,3,2))
print(tambah(4,5,6,7,4,3))

# print(naruto.narutoAuthor())
# print(naruto.resengan("rasen suriken"))
print(anime.naruto.narutoAuthor())

# print(fs.percepatan(130, 384))
# print(fs.gaya(123, 49.8))
print(fisika.testSaja.percepatan(34, 32))
print(fisika.testSaja.gaya(24, 32))



tEnd = time.time()
print(f"waktu eksekusi {tEnd - tStart}")

