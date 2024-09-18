import os

os.system("clear")

# PANJANG = int(input("Masukkan panjang : "))
# LEBAR = int(input("Masukkan lebar : "))

# Keliling
def keliling(panjang, lebar):
    return 2 * (panjang * lebar)

# Luas
def luas(panjang, lebar) :
    return panjang * lebar

# print(keliling(PANJANG, LEBAR))
# print(keliling(lebar= 10, panjang=PANJANG))
# print(luas(lebar=10, panjang=30))

# Kalkulator
def calculator (*angka, **aritmatika) :
    a = 0
    if aritmatika["operator"] == "+" :
        print("+")
        for i in angka :
            a += i
        return a
    elif aritmatika["operator"] == "-" :
        print("-")
        for i in angka :
            a -= i
        return a
    elif aritmatika["operator"] == "*" :
        print("*")
        hasil = 1
        for i in angka :
            hasil *=i
        a = hasil
        return a
    else :
        return "OK"

print(calculator(2,3,4, operator="+"))
print(calculator(10,14,4,5,5,5, operator="-"))
print(calculator(3,5,5, operator="*"))
print(calculator(143, 3,2, operator="/"))