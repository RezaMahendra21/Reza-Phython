import collections

# SOAL UTS NO 3

# nilai awal deque
de = collections.deque([10, 11, 12,])
print("nilai awal deque adalah : ")
print (de)

# deque setelah ditambahkan dari ujung kiri
de.extendleft([13, 14,])
print("deque setelah ditambahkan dari ujung kiri : ")
print (de)

# deque setelah ditambahkan dari ujung kanan
de.extend([15, 16,])
print("deque setelah ditambahkan dari ujung kanan : ")
print (de)

# deque setelah nilai 20 dihapus
# e.remove(20)
# print("deque setelah dihapus 20 : ")
# print (de)

# deque setelah diputar 
de.rotate(-2)
print("deque setelah diputar adalah  : ")
print (de)
