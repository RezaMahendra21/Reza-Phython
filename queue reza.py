import collections

# program dequeue
de = collections.deque([1, 2, 3,])

print("Nilai awal deque adalah : ")
print (de)

#menggunakan extend() untuk menambahkan angka keujung kanan
# menambahkan angka (4 5 6) ke ujung kanan
de.extend ([4,5,6])
print ("Deque setelah ditambahkan dari ujung kanan : ")
print (de)

#menggunakan extendleft() untuk menambahkan angka ke ujung kiri
# menambahkan (7,8,9) ke ujung kiri
de.extendleft([7,8,9])
print ("deque setelah ditambah dari ujung kiri : ")
print (de)

# menggunakan rotate() untuk memutar deque
# Berputar 1 kekiri
de.rotate(-1)
print ("deque setelah diputar adalah : ")
print (de)

# Reverse() untuk membalikkan deque
de.reverse()

print ("deque setelah membalikkan deque adalah : ")
print (de)
