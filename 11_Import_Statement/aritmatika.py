
def tambah(*args) :
    hasil = 0
    for n in args :
        hasil += n
    return hasil

def kali(*args) :
    hasil = 1
    for n in args :
        hasil *= n
    return hasil

# print(tambah(2,4,5))
# print(kali(3,5,2))