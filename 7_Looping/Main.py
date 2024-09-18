RezaMahendra = ["a", "n", "d"]

RezaMahendra.insert(0, "u")
RezaMahendra.remove("u")
RezaMahendra.append("r")
RezaMahendra.append("i")
RezaMahendra.pop(1)

# i = 0
# for el in Reza Mahendra :
#     print(f"indek ke-{i} : {el}"  )
#     i+=1

# for i in range(40) :
#     print(f"index ke- {i} : {i + 1}")
    

# While
# nilai = 1
# while nilai <= 10 :
#     print(f"index ke-OK")
#     nilai+=1

# for i in range(3) :
#     for j in range(3) :
#         if i == j :
#             print("*".center(3)*(i+1))

# BMI
# condition = True
# while condition == True :
#     tinggi = int(input("Tinggi badan : "))
#     berat = int(input("Berat badan : "))
#     bmi = berat / tinggi
#     print(f"BMI kamu adalah : {bmi}")
#     temp = input("Hitung Lagi ? : (y/n) \t")
#     if temp == "y" :
#         condition = True
#     else :
#         condition = False

# Continue
counter = 0
while counter < 10 :
    counter += 1
    if counter == 7 :
        print("Halo")
        print("Gak ada 7")
        continue
    print(f"Iy bro ke-{counter}")

# Break
print("---------------------------")
counter = 0
while counter < 10 :
    counter += 1
    if counter == 5 :
        print ("halo")
        print("gak ada 5")
        break
    print(f"iya bro ke-{counter}")