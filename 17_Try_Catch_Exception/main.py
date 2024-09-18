from numbers import Number

try :
    with open("./17_Try_Catch_Exception/try.txt", encoding="utf-8", mode="r") as fileR :
        data = fileR.read()
        print(data)
except :
    with open("./17_Try_Catch_Exception/try.txt", encoding="utf-8", mode="w") as fileW :
        fileW.write("lorem ipsum")
    print("Ok")  

# membuat exception
def tambah(a, b) :
    if not isinstance(a, Number) or not isinstance(b, Number) :
        raise "input harus angka" 
    return a + b
# tambah("a", 5)
# tambah(4, "c")
print(tambah(3,5))

angka = int(input("masukkan angka : "))
try :
    hasil = 10/angka
except Exception as err :
    print(f"msg : {err}")
