
namaKeluarga = ["RezaMahendra", "Nia", "Liana", "Ali",]
# print(namaKeluarga)

# for i in namaKeluarga : 
#     print(f"Nama : {i}")

# dataRange = range(0, 10, 2) #range(start, stop, step)
# # print(list(dataRange))

# list_for = [i*2 for i in range(10)]
# # print(list_for)

# list_for = [i for i in range(10) if i != 4]
# # print(list_for)

# list_for = [i for i in range(10) if i%2 == 0]
# # print(list_for)

# # print(f"nama : {namaKeluarga[-1]}")
# # print(f"panjang : {len(namaKeluarga)}")

# dataBaru = ["Kucing", "Laptop", "Rumah"]

# print(namaKeluarga)
# # Tambah Data sesuai Index
# namaKeluarga.insert(3, "Hadi")
# # Tambah data diakhir 
# namaKeluarga.append("Nadine")
# print(namaKeluarga)
# # menggabungkan antar list
# namaKeluarga.extend(dataBaru)
# print(namaKeluarga)
# # Mengapus data sesuai 
# namaKeluarga.remove("Kucing")
# print(namaKeluarga)
# # Menghapus data diakhir
# namaKeluarga.append("OOOJOJO")
# print(namaKeluarga)
# namaKeluarga.pop()
# print(namaKeluarga)

# print("-------------------------")
# namaKeluarga.sort()
# print(namaKeluarga)
# namaKeluarga.reverse()
# print(namaKeluarga)

# namaKeluarga[0] = "Muhammad Andrian"
# kepalaKeluarga = namaKeluarga.copy()
# print(namaKeluarga)
# print()
# print(hex(id(namaKeluarga)))
# print(kepalaKeluarga)

# List bersarang
dataDiri = ["RezaMahendra", 21, ["smk n 1 jarai", "s1 teknik informatika", "S1 teknik informatika"], "programmer"]

print(dataDiri)
print("-----------------")
# for data in dataDiri :
#     print(data)
    # for dt in dataDiri[2] : 
    #     print(f"data : {dt}")
    #     continue;

# dataDiri.count()

# for data in range(len(dataDiri)) :
#     print(f"data pada index ke-{data} : {dataDiri[data]}")
#     if data == 2 :
#         for dt in range(len(dataDiri[2])) :
#             print(f"index k2 : {dataDiri[2][dt]}" )

# k1 = ["Andrian", 21, "Programmer"]
# k2 = ["Nia", 19, "Data Analis"]
# k3 = ["Liana", 2, "Anak"]

# gabung = [k1, k2, k3]
# print(gabung)

# i = 0
# for data in gabung :
#     for l in data :
#         print(f"data : {l}")
#     print("\n")

for index, data in enumerate(dataDiri) :
    print(f"index ke-{index} - data : {data} | \n")

[print(f"data: {i}") for i in dataDiri]