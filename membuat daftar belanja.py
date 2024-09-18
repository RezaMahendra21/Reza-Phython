2# membuat daftar belanja

# menambah daftar Belanja
def tambah_belanja(text):
    file = open('belanja.txt', 'a+')
    file.write('\n' + text)
#list Belanja
def daftar_belanja():
    file = open('belanja.txt', 'a+')
    file.seek(0)
    text = file.read()
    print(text)
# tentang Apps
def tentang_program():
    tentang = open('about.txt', 'r')
    app = tentang.read()
    print(app)

def membaca_daftar_source_code():
    kode = open('source.txt', 'r')
    apps = kode.read()
    print(apps)


def tanya_pengguna():
    print('Silahkan Masukan Keperluan Belanja anda Ke daftar Belanja')
    print('====================== Daftar Belanja ===================')
    tambah_belanja(input('Mau Belanja Apa :  '))


loop = True

print('================== Menu ==============')
print('1. Tambah ke Daftar Belanja')
print('2. List Belanja')
print('3. Quit/ Keluar')
print('4. About Apps')
print('5. view code')
print('======================================')
while (loop):
    print('\n')
    menu = input('Masukan menu = ')

    if menu == "1":
        tanya_pengguna()
    elif menu == "2":
        daftar_belanja()

    elif menu == "3":
        quit()

    elif menu == "4":
        tentang_program()
    elif menu == "5":
        membaca_daftar_source_code()
    else:
        print("command not found")