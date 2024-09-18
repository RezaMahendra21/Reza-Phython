mat1 = [
    [5, 2, 1],
    [7, 9, 2],
    [5, 2, 3],
]

mat2 = [
    [1, 2, 2],
    [5, 5, 2],
    [1, 2, 2],
]

hasil = []
for i in range(len(mat1)):
    baris = []
    for k in range(len(mat2[0])):
        val = 0
        for j in range(len(mat1[i])):
            val += mat1[i][j] + mat2[j][k]
        baris.append(val)
    hasil.append(baris)

print("Hasil Penjumlahan 2 matriks adalah:")
for baris in hasil:
    print(baris)