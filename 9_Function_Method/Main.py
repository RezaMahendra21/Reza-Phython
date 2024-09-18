import datetime as dt
import os

os.system("clear")

# Function luas segitiga
def andrian():
    print("Reza Mahendra")

def seigitiga (panjang, lebar) :
    return (1/2) * panjang * lebar

def salam(nama = "And19", waktu = "Pagi") :
    return(f"Selamat {waktu}, {nama}")

# print(seigitiga(4, 4))
# print(seigitiga(7,3))
# andrian()

# print(salam("Andrian", "sore"))

def salamBanyak (peserta) :
    for nama in peserta : 
        print(f"Halo {nama} !")


# salamBanyak(["Reza Mahendra", "Nia", "Ali", "Hadi", "Liana"])
# print(salamBanyak(["Reza Mahendra", "Nia", "Ali", "Hadi", "Liana"]))

def kuadrat(angka) :
    return angka ** 2

# print(kuadrat(5))

def operasiMatematika (a, b) :
    tambah = a + b
    kali = a * b
    kurang = a - b
    bagi = a / b
    return tambah, kali, kurang, bagi

# print(operasiMatematika(5,9))

a, b, c, d = operasiMatematika(8, 2)
# print(f"tambah {a}")
# print(f"tambah {b}")
# print(f"tambah {c}")
# print(f"tambah {d}")

# print(salam())

# Hints argument
def pangkat(angka:int, pangkat:int = 2) : 
    return angka ** pangkat

# print(pangkat(9))
# print(pangkat(5, 3))
# print(pangkat(angka=6, pangkat=5))
# print(pangkat(pangkat=3, angka=5))

waktuSekarang = dt.date.today()
# print(waktuSekarang)

# Hinst argument function
def dataSaya (nama:str, ttl:int) -> str :
    return f"Nama Saya {nama}, umur : {waktuSekarang.year - ttl}"

# print(dataSaya(nama="Andrian", ttl=2001))
# print(dataSaya("Nia", 2003))


# *args ==> dimamic parameter
# returnya dalam bentuk tupples
def bioSaya(*saya) -> str :
    return f"Nama saya {saya[0]} umur saya {saya[1]}"

def totaParams(*ankga:int) -> int :
    hasil = 0
    for i in ankga :
        hasil += i
    return hasil
    
print(bioSaya("Reza Mahendra", 20))
print(totaParams(1,2,3,4,5,6))

# **kwargs
# returnya dalam bentuk set
def sayaAdalah(**saya) :
    return f"Nama Saya {saya['nama']} umur {saya['umur']}"
# isi paremeter dngn key dan value
print(sayaAdalah(nama="Reza Mahendra", umur=21))