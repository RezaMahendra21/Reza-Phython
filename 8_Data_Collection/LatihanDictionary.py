import datetime
import random
import os

andrian = {
    "nama" : "RezaMahendra",
    "nim" : "20420107",
    "ttl" : datetime.date(2001, 4, 5)
}
nia = {
    "nama" : "Nia",
    "nim" : "19191919",
    "ttl" : datetime.date(2003, 6, 22)
}

kumpulanMhs = {
    "MHS1" : andrian,
    "MHS2" : nia
}

print(kumpulanMhs)

pesan = """
Pilih:
1> Input Data
2> Lihat Data
3> Update Data
4> Hapus Data
* Keluar
"""
kondisi = True

while kondisi == True : 
    pilihan = input(pesan)
    if pilihan == "1" :
        mhs = {
            "nama" : input("Masukkan nama : "),
            "nim" : input("Masukkan nim : "),
            "ttl" : input("Masukkan TTL : ")
        }
        kumpulanMhs.update(
            {
                f"MHS{str(random.randrange(100, 999))}" : mhs
            }
        )
        os.system('clear')
        print(kumpulanMhs)
    else :
        kondisi = False


