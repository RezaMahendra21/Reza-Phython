# Program Mengurutkan Terbesar ke Terkecil
def arrayDescending(Data):
         for i in range(len(Data)):
           for j in range(i+1,len(Data)):
            if(Data[i] < Data[j]):
                temp = Data[i]
                Data[i]=Data[j]
                Data[j]=temp

Data= ['80','45','90','75','45','50','80','95','60']
arrayDescending(Data)
print("Output terkecil ke terbesar : ",Data)
