# PROGRAM MENENTUKAN BILANGAN

angka_awal = int(input('Masukkan Angka Awal : '))
angka_akhir = int(input('Masukkan Angka Akhir : '))

list_angka = [i for i in range(angka_awal, angka_akhir +1 )]

bilangan_prima = [i for i in list_angka if (i==2 or i==3 or i==5 or i==7)
or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 )]

print('Bilangan Prima',angka_awal,("sampai"),angka_akhir,("adalah : "),(bilangan_prima))
