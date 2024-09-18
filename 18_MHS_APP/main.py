import os

import View.MhsView as mhsView
import Model.MhsModel as mhsModel

os.system("clear")

# Properti Input
ID = ""
NAMA = ""
JURUSAN = ""

def formInput() : 
    ID = input("Masukkan ID : ")
    NAMA = input("Masukkan NAMA : ")
    JURUSAN = input("Masukkan Jurusan : ")
    data = {
        "ID" : ID,
        "NAMA" : NAMA,
        "JURUSAN" : JURUSAN
    }
    return data

# Main 
while True :
    # Head APP
    mhsView.headMhs()
    selected = int(input("Pilih : "))
    if selected == 1 :
        mhsView.headTableMhs()
        mhsView.readMhs()
    elif selected == 2 :
        data = formInput()
        mhsModel.insertMhs(ID=data["ID"], nama=data["NAMA"], jurusan=data["JURUSAN"])
    elif selected == 3 :
        mhsByName = input("Masukkan Nama : ")
        mhsView.readMhsByName(mhsByName)
        data = formInput()
        mhsModel.updateMhsByName(oldName=mhsByName, nama=data["NAMA"], jurusan=data["JURUSAN"])
    elif selected == 4 :
        mhsByName = input("Masukkan Nama : ")
        mhsView.readMhsByName(mhsByName)
        dataMhs = mhsModel.getMhsByName(mhsByName)
        try :
            hapus = input("Hapus ? : y/n ")
            if hapus == "y" :
                mhsModel.deleteMhsById(dataMhs['id'])
        except Exception as err :
            print(err)
    elif selected == 5 :
        mhsByName = input("Masukkan Nama : ")
        mhsView.readMhsByName(mhsByName)
    else :
        break

