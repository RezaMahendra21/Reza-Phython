# NAMA : REZA MAHENDRA
# NIM  : 20420107
# KELAS: 3D
# InsertionSort asscending dan descending
def InsertionSort(val):
    for isi in range(len(val)-1,0,-1):
        max=0
        for lokasi in range(1,isi+1):
            if val[lokasi]>val[max]:
                max = lokasi

        temp = val[isi]
        val[isi] = val[max]
        val[max] = temp

def arrayDescending(Data):
         for i in range(len(Data)):
           for j in range(i+1,len(Data)):
            if(Data[i] < Data[j]):
                temp = Data[i]
                Data[i]=Data[j]
                Data[j]=temp

Data= ['C','I','N','T','A','B','U','N','D','A']
InsertionSort(Data)
print("Setelah di selectionsort secara asscending : ",Data)
arrayDescending(Data)
print("Setelah di selectionsort secara Descending : ",Data)