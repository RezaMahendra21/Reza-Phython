
import datetime as dt

ttl = dt.date(2001, 4, 14)
waktuSekarang = dt.date.today()

umurHari = waktuSekarang - ttl
umurTahun = umurHari // 365
umurBulan = (umurHari.days % 365) // 30
berapaHari = waktuSekarang.day - ttl.day

print(umurHari.days)
print(umurTahun.days)
print(umurBulan)
print(berapaHari)

boiData = f"""
Nama saya , Reza Mahendra umur saya {umurTahun.days} tahun, {umurBulan} bulan, {berapaHari} hari.
"""

print(boiData)
print("Berapa hari lagi kamu ultah?")

ultah = dt.date(2023, 4, 5)

hari = ultah - waktuSekarang
print(hari.days)
berapaBulan = hari.days // 30
print(berapaBulan)

berapaHariLagi = hari.days % 30
print(berapaHariLagi)

apaaja = umurHari.days + 365
print(apaaja - umurHari.days)

apaaja2 = (umurBulan * 30) + berapaHari
print(apaaja - apaaja2)
apaaja2 = apaaja - apaaja2

bulan1 = (apaaja2 - umurHari.days) // 30
hariAsal = (apaaja2 - umurHari.days) % 30
print(bulan1)
print(hariAsal)