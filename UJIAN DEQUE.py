import collections

# SOAL UTS NO 3

# nilai awal deque
de = collections.deque(['K', 'O', 'T','A'])
print("nilai awal deque adalah : ")
print (de)

# deque setelah ditambahkan dari ujung kiri
de.extendleft(['M','S','A'])
print("deque setelah ditambahkan dari ujung kiri : ")
print (de)

# deque setelah ditambahkan dari ujung kanan
de.extend(['B','U','A'])
print("deque setelah ditambahkan dari ujung kanan : ")
print (de)

# deque setelah nilai 20 dihapus
# e.remove(20)
# print("deque setelah dihapus 20 : ")
# print (de)

# deque setelah diputar 
de.rotate(1)
print("deque setelah diputar adalah  : ")
print (de)

# deque setelah dIBALIK
de.reverse()
print("deque setelah diputar adalah  : ")
print (de)
