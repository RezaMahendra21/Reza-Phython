prog = ["PHP", "JS", "Dart", "Python"]

dataDiri = {
    "nama" : "Reza Mahendra",
    "nim" : 20420107,
    "jurusan" : "s1 teknik informatika",
    "prog" : prog
}


# print(dataDiri.get("nama"))
# print(dataDiri.get("prog"))
# print(dataDiri.keys())
# print(dataDiri.values())
# print(dataDiri.items())

# Mengupdate key
dataDiri["nim"] = 20420107
# print(dataDiri.get("nim"))
dataDiri.update({"nim" : "20420107"})
# print(dataDiri.get("nim"))

# Menambah / Mengupdate
# dataDiri.update({"hobi" : "Gak Ada"})

# Menambah key
dataDiri["status"] = "programmer"
# print(dataDiri)

# Looping
# for saya in dataDiri :
#     print(f"{saya} : {dataDiri.get(saya)}")

# for value in dataDiri.values() :
#     print(f"value : {value}")
# for item in dataDiri.items() :
#     print(f"item : {item}")
# for key, value in dataDiri.items() :
#     print(f"key : {key} - value : {value}")

dataAnd = dataDiri.copy()
print(dataDiri)
print(dataAnd)
dataAnd.update({"nim" : "48343484834"})
print(dataAnd)
print(dataDiri)

# menghapus data berdasarkan key
dataAnd.pop("nama")
print(dataAnd)
# menghapus item terakhir
dataAnd.popitem()
print(dataAnd)