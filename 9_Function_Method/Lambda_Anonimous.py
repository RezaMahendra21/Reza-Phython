import os

os.system("clear")

# Lamda function
kuadrat = lambda angka:angka**2
# print(kuadrat(5))

saya = lambda nama, umur, alamat : f"Nama Saya {nama}, {umur} tahun, asal {alamat}"

# print(saya("Andrian", 21, "Sapaga Jatibaru Barat"))

def funcPanjangNama(nama:str) -> int :
    return len(nama)
# print(funcPanjangNama("Ciment"))

panjangNama = lambda nama : len(nama)
# print(panjangNama("Rahmat Ali Tcandra"))

dataList = ["Reza Mahendra", "Cimen", "Ali", "Hadi"]
dataList.sort(key=lambda nama:len(nama), reverse=True)
# print(dataList)

dataNilai = [1,2,4,5,6,7,8,9]
dataNilaiBaru = list(filter(lambda a : a > 5, dataNilai))
# print(dataNilai)
# print(dataNilaiBaru)

dataBaru = list(filter(lambda nilai : nilai % 2 == 0, dataNilai))
# print(dataBaru)

dataBaru.sort()
dataBaru.reverse()
# print(dataBaru)

# anonymous fnc
def pangkat(n) :
    return lambda ankgka: n**ankgka
# print(pangkat(3)(2))
# pangkat2 = pangkat(3)
# print(pangkat2(2))
# pangkat3 = pangkat2(5)
# print(pangkat3)

def dataDiriSaya(nama) :
    return lambda saya: f"Nama Saya {nama} saya {saya}"
perkenalan = dataDiriSaya("Reza Mahendra")
print(perkenalan("OKkK"))
perkenalan2 = dataDiriSaya("Dia")
print(perkenalan2("Yeee"))