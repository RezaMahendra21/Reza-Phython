# NAMA : REZA MAHENDRA
# NIM  : 20420107
# KELAS: 3D
# InsertionSort asscending dan descending
def CommonSort(val):
    for isi in range(len(val)-1,0,-1):
        max=0
        for lokasi in range(1,isi+1):
            if val[lokasi]>val[max]:
                max = lokasi

        temp = val[isi]
        val[isi] = val[max]
        val[max] = temp

def ExchangeSort(Data):
         for i in range(len(Data)):
           for j in range(i+1,len(Data)):
            if(Data[i] < Data[j]):
                temp = Data[i]
                Data[i]=Data[j]
                Data[j]=temp

Data= ['110','30','5','90','20','70','60','10','15']
CommonSort(Data)
print("Setelah di commonSort : ",Data)
ExchangeSort(Data)
print("Setelah di ExchangeSort : ",Data)