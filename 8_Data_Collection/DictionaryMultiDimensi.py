import datetime as dt

RezaMahendra = {
    "nama" : "RezaMahendra",
    "nim" : "20420107",
    "prog" : ["PHP", "JS", "Python", "Java", "Dart"]
}

ali = {
    "nama" : "Ali",
    "nim" : "191919191",
    "prog" : ["JS", "Python", "Java"]
}
nia = {
    "nama" : "Nia",
    "nim" : "2201010101",
    "prog" : ["JS", "Python", "Dart"]
}

keluarga = {
    "K1" : RezaMahendra,
    "K2" : nia,
    "K3" : ali
}

print(f"{'Key':<6} {'Nama': <17} {'Nim':<11} {'Prog':<30}")
for data in keluarga : 
    print(f"{data:<6} {keluarga[data].get('nama'):<17} {keluarga[data].get('nim'):<11} {keluarga[data].get('prog')}")

# ttl = dt.datetime(2001, 4, 4)
# print(ttl)
# print(ttl.now())
# # print(ttl.isocalendar())
# print(ttl.today())

