import os

os.system('clear')

fileRead = open("./16_RW_File/text.txt", mode='r')

# print(fileRead.readlines())
# Baca perbaris
# print(fileRead.readline()) 
# print(fileRead.readline(), end="")
# Baca semua
print(fileRead.read())

# cek bisa dibaca/ditulis
# print(fileRead.readable())
# print(fileRead.writable())

# cek close
print(fileRead.closed)
fileRead.close()
print(fileRead.closed)

with open(file="./16_RW_File/text.txt", mode='r') as fileRead2 :
    # print(fileRead2.read())
    # print(fileRead2.readlines(), end="")
    print(fileRead2.closed)

print(fileRead2.closed)

