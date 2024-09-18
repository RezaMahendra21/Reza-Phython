# data buku = [["Judul Buku", "Penulis", "tahun terbit", "harga"]]

dataBuku = [
    ["Naruto 1", "Masashi Kishimoto", "1997", 85000],
    ["Naruto 2", "Masashi Kishimoto", "1999", 90000],
]

kondisi = True
pesan = """
Pilih :
1 > Tambah Buku
2 > Hapus Buku
3 > Edit Buku
4 > Lihat Buku
"""
judulBuku = ""
penulis = ""
tahunTerbit = ""
harga = ""
while kondisi == True : 
    pilihan = input(pesan)
    if pilihan == "1" : 
        judulBuku = input("Masukkan Judul Buku : ")
        penulis = input("Masukkan Penulis Buku : ")
        harga = input("Masukkan Harga Buku : ")
        print("Buku Telah Ditabahkan")
        dataBuku.insert(0, [judulBuku, penulis, harga])
        print(dataBuku)
    elif pilihan == "2" :
        hapus = input("Masukkan nama buku yang ingin dihapus : ")
        for buku in dataBuku :
            if buku[0] == hapus :
                dataBuku.remove(buku)
                print("Buku Telah dihapus")
                print(dataBuku)
                break
    elif pilihan == "3" :
        editBuku = input("Masukkan nama Buku : ")
        for i in dataBuku : 
            if i[0] == editBuku :
                print(i)
                editBuku = i[0]
                judulBuku = input("Masukkan Judul Buku : ")
                penulis = input("Masukkan Penulis Buku : ")
                harga = input("Masukkan Harga Buku : ")
                i[0] = judulBuku
                i[1] = penulis
                i[2] = harga
                break
        print(dataBuku)
    elif pilihan == "4" :
        print("Data Buku".center(6, "-"))
        print("|Nama Buku \t | Penulis \t | Harga Buku \t |")
        for buku in dataBuku : 
            print(f"|{buku[0]} \t | {buku[1]} \t | {buku[2]}")
    else :
        print("Ok")
        kondisi = False
    

