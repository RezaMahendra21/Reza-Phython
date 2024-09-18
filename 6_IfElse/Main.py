

# Kalkulator

angka1 = int(input("Masukkan angka 1 : "))
operator = input("Masukkan Operator ")
angka2 = int(input("Masukkan angka 2 : "))

if operator == "+" :
    angka1 += angka2
elif operator == "-" :
    angka1 -= angka2
elif operator == "*" :
    angka1 *= angka2
elif operator == "/" :
    angka1 /= angka2

print(f"Hasil : {angka1}")