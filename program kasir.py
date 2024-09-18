# membuat program kasir resto sederhana
def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
     
    else:
        print('input program salah harap ulangi')
 
def kasir():
    # masukan input dari user
    nama_barang = input('masukan pesanan anda: ')
    harga = int(input('masukan harga barang: '))
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
 
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()
 
 
def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. Program kasir')
    print('2. program kalkulator')
    print('3. exit program')
 
    # input pilihan
    pilihan = input('pilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('program exit')
        exit()
 
 
# membuat fungsi authentifikasi sederhana
def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
 
    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')
 
# membuat kalkulator
def kalkulator():
    print('=' * 10)
    print('Program Kalukator')
 
    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang ')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')
 
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan ke-dua: '))
 
    operator = input('masukan operator: ')
 
    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukan input yang benar sesuai menu diatas')
 
# main program
if __name__=='__main__':
    get_login()