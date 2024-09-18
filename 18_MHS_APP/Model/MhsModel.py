import json
import os
os.system("clear")

def openJson() :
    with open("./18_MHS_APP/Model/mahasiswa.json") as mhs :
        data = json.load(mhs)
        data = data['data']
    return data

# print(openJson())
dataAsli = {}

def writeToJson(dataMhsJson) :
    dataAsli["data"] = dataMhsJson
    json_object = json.dumps(dataAsli, indent=2)
    with open("./18_MHS_APP/Model/mahasiswa.json", mode="w", encoding="utf-8") as writeMhs :
        writeMhs.write(json_object)
    
def getMhs () : 
    return openJson()

def insertMhs(**data) :
    dataMHs = openJson()
    dataInput = {
        "id" : data["ID"],
        "nama" : data["nama"],
        "jurusan" : data["jurusan"]
    }
    dataMHs.append(dataInput)
    try :
        writeToJson(dataMHs)
        print("="*5, "data berhasil diinput", "="*5)
    except Exception as err :
        print(err)

def getMhsByName (name:str) -> list :
    data = openJson()
    for dt in data :
        if dt['nama'] == name :
            return dt
    return "Nama tidak ditemukan.."

def updateMhsByName (oldName, **mhs) :
    try :
        # Mencari data Mhs Yang Cocok
        mhsJson = openJson()
        for dt in mhsJson :
            if dt['nama'] == oldName :
                dt['nama'] = mhs["nama"]
                dt['jurusan'] = mhs["jurusan"]
                print(dt)
        writeToJson(mhsJson)
        print("="*5, "Data Telah diupdate", "="*5)
    except Exception as err :
        print(f"error : {err}")

def deleteMhsById(mhsId) :
    try :
        mhs = openJson()
        print(mhs)
        for dt in mhs :
            if dt['id'] == mhsId :
                mhs.remove(dt)
                print(mhs)
                writeToJson(mhs)
                print("="*5, "Data Telah dihapus", "="*5)
                return
        print("="*5, "Data Tidak ditemukan", "="*5)
    except Exception as err :
        print(err)
