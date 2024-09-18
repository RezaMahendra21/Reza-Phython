
namaDepan = "Reza"
namaBelakang = "Mahendra"

namaPanjang = namaDepan + " " + namaBelakang
print("Nama Saya : ", namaPanjang)

print(len(namaPanjang))

print(namaPanjang.count("a"))
print(namaPanjang.find("M"))
print(namaPanjang.upper())
print("And" in namaPanjang)
print("and" in namaPanjang)
print("And" not in namaPanjang)
print("and" not in namaPanjang)

print(namaBelakang * 5)

print(namaPanjang[0])
print(namaPanjang[3])

print(namaBelakang.islower())
namaBaru = namaBelakang.lower()
print(namaBaru.islower())
print(namaBaru.isupper())
print(namaPanjang.istitle())

alay = ["aku", "sayang", "kamu"]
alay2 = "-".join(alay)
print(alay2)
print(alay2.endswith("kamu"))

print(alay2.split("-"))

print(namaPanjang.center(20, "="))

# Format String

umur = 20
isJomblo = False

iya = "iya"
gak = "gak"

nilaiUlangan = 98.2
tabungan = 20000000

format_str = f"Nama Saya : {namaPanjang}, umumr saya {umur:d}, status {iya if isJomblo == True else gak}, nilai ulangan {nilaiUlangan}, tabungan {tabungan:,}"
print(format_str)