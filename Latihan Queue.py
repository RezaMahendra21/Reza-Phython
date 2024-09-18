import collections

# program dequeue
de = collections.deque([10, 11, 12,])

print("Nilai awal deque adalah : ")
print (de)

#menggunakan extendleft() untuk menambahkan angka ke ujung kiri
# menambahkan 13,4 ke ujung kiri
de.extendleft([13,14])
print ("deque setelah ditambah dari ujung kiri : ")
print (de)

#menggunakan extend() untuk menambahkan angka keujung kanan
# menambahkan angka 15, 16 ke ujung kanan
de.extend([15,16])
print ("Deque setelah ditambahkan dari ujung kanan : ")
print (de)

# menggunakan rotate() untuk memutar deque
# Berputar 2 kekiri
de.rotate(-2)
print ("deque setelah diputar adalah : ")
print (de)

# Reverse() untuk membalikkan deque
de.reverse()

print ("deque setelah membalikkan deque adalah : ")
print (de)
