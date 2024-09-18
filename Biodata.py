def get_biodata():
    nama = input('input nama: ')
    alamat = input('input alamat: ')
    ttl = input('input tempat dan tanggal lahir: ')
    pekerjaan = input('input pekerjaan: ')
    status = input('input status: ')
    print('================================')
    print('Biodata anda adalah: ')
    print('nama: ' + nama)
    print('alamat: ' + alamat)
    print('ttl: ' + ttl)
    print('pekerjaan: ' + pekerjaan)
    print('status: ' + status)
 
def run():
    while True:
        get_biodata()
        input_lagi = input('apakah input lagi? (y/n): ')
        if input_lagi == 'y':
            continue
        elif input_lagi == 'n':
            break
 
if __name__ == '__main__':
    run()