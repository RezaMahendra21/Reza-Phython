import os
import queue

class myQueue:
    def __init__(self):
        self.items = queue.Queue()

    # memeriksa apakah queue dalam keadaan kosong 
    def isEmpty(self):
        return self.items.empty()
    # menambah data ke queue
    def qput(self, item):
        self.items.put(item)
    # mengeluarkan data dari queue
    def qGet(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "empty"
    # menghitung panjang queue
    def size(self):
        return self.items.qsize()
    # main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("==============================================")
            print("|               menu aplikasi queue      |")
            print("==============================================")
            print("1. menambahkan data di antrian")
            print("2. menghapus data di antrian")
            print("3. cek empty")
            print("4. panjang dari antrian/queue")
            print("==============================================")
            pilihan=str(input(("silahkan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("cls")
                antrian = str(input("masukan antrian yang ingin ditambahkan: "))
                self.qput(antrian)
                print("antrian "+antrian+" telah ditambahkan")
                x = input("")
            elif(pilihan=="2"):
                os. system("cls")
                temp = self.qGet()
                if temp != "empty":
                    print("Antrian "+temp+" dihapus")
                else:
                    print("Antrian/Queue kosong")
                x = input("")
            elif(pilihan=="3"):
                os.system("cls")
                print(self.isEmpty())
                x = input("")
            elif(pilihan=="4"):
                os.system("cls")
                print("panjang dari queue adalah: "+str(self.size()))
                x = input("")
            else:
                pilih="n"

if __name__ == "__main__":
    q=myQueue()
    q.mainmenu()