import Model.MhsModel as mhsModel
mhsAttr = {
    "ID" : "ID",
    "NAMA" : "Nama",
    "JURUSAN" : "Jurusan"
}

def headMhs() :
    print("\n")
    print("="*5, "MHS APP", "="*5)
    print("1. Lihat MHS")
    print("2. Tambah MHS")
    print("3. Edit MHS")
    print("4. Hapus MHS")
    print("5. Detail MHS")
    print("6. Exit()")

def headTableMhs (detailMode = False) :
    if detailMode == False :
        print("="*40)
        print("|", f"{mhsAttr['ID']:10} |", f"{mhsAttr['NAMA']:20} |")
    else :
        print("="*60)
        print("|", f"{mhsAttr['ID']:10} |", f"{mhsAttr['NAMA']:20} |", f"{mhsAttr['JURUSAN']:20}")
    
def readMhs() :
    dataMhs = mhsModel.getMhs()
    for dt in dataMhs :
        print("|", f"{dt['id']:10} |", f"{dt['nama']:20} |")
    print("="*40)

def readMhsByName(name) :
    try :
        mhs = mhsModel.getMhsByName(name)
        headTableMhs(detailMode=True)
        print("|", f"{mhs['id']:10} |", f"{mhs['nama']:20} |", f"{mhs['jurusan']:20} |")
        print("="*60)
    except :
        print(mhs)
