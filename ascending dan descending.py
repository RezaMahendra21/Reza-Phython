# program ascending dan descending pada phython
def SelectionSort(val):
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

Data= ['S','E','K','O','L','A','H','O','N','L','I','N','E']
SelectionSort(Data)
print("Output secara asscending : ",Data)
arrayDescending(Data)
print("Output secara Descending : ",Data)