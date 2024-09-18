umur = input("masukan umur: ")
if int(umur) < 45:
    keterangan = 'masih muda'
else: 
    keterangan = 'sudah tua'
 
print('anda memasukan umur {}, artinya {}'.format(umur, keterangan))