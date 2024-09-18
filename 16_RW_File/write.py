
# mode write
with open('./16_RW_File/text.txt', mode="w", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("Reza Mahendra")

# mode (a) append ==> menambahkan text diakhir
with open('./16_RW_File/text.txt', mode="a", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\nsaya adalah Reza Mahendra, saya akan menjadi programmer.!")

# menimpa hanya pada baris tertentu
with open('./16_RW_File/text.txt', mode="r+", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\nsaya adalah Reza Mahendra, saya akan menjadi programmer.!")

with open('./16_RW_File/text.txt', mode="r+", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\nsaya adalah Reza Mahendra, saya akan menjadi programmer.!")
