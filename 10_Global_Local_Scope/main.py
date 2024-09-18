
namaGlobal = "Reza Mahendra"
print(namaGlobal)

def sapa(nama) :
    global namaGlobal
    namaGlobal = nama
    return namaGlobal

sapa2 = lambda nama : f"Nama saya {nama}"

print(sapa("OK"))
print(sapa2("Cimenr"))