
from bangun_datar import *

# Menggunakan fungsi-fungsi dari modul bangun_datar
sisi_persegi = 7
panjang_persegi_panjang = 9
lebar_persegi_panjang = 10
jari_jari_lingkaran = 9
alas_segitiga = 6
tinggi_segitiga = 7
alas_trapesium = 5
alas_bawah_trapesium = 8
tinggi_trapesium = 2
alas_jajar_genjang = 3
tinggi_jajar_genjang = 8

# Menghitung luas dan keliling
print(f"Luas Persegi: {luas_persegi(sisi_persegi)}")
print(f"Keliling Persegi: {keliling_persegi(sisi_persegi)}")

print(f"Luas Persegi Panjang: {luas_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)}")
print(f"Keliling Persegi Panjang: {keliling_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)}")

print(f"Luas Lingkaran: {luas_lingkaran(jari_jari_lingkaran)}")
print(f"Keliling Lingkaran: {keliling_lingkaran(jari_jari_lingkaran)}")

print(f"Luas Segitiga: {luas_segitiga(alas_segitiga, tinggi_segitiga)}")
print(f"Keliling Segitiga: {keliling_segitiga(sisi_persegi, sisi_persegi, sisi_persegi)}")

print(f"Luas Trapesium: {luas_trapesium(alas_trapesium, alas_bawah_trapesium, tinggi_trapesium)}")
print(f"Keliling Trapesium: {keliling_trapesium(sisi_persegi, sisi_persegi, sisi_persegi, sisi_persegi)}")

print(f"Luas Jajar Genjang: {luas_jajar_genjang(alas_jajar_genjang, tinggi_jajar_genjang)}")
print(f"Keliling Jajar Genjang: {keliling_jajar_genjang(sisi_persegi, sisi_persegi)}")



# Aritmatika

# Contoh penggunaan modul aritmatika

import aritmatika

# Menggunakan fungsi dari modul aritmatika
hasil_penjumlahan = aritmatika.tambah(2, 5)
hasil_pengurangan = aritmatika.kurang(13, 6)
hasil_perkalian = aritmatika.kali(3, 4)
hasil_pembagian = aritmatika.bagi(21, 3)
hasil_perpangkatan = aritmatika.pangkat(3, 5)
hasil_modulus = aritmatika.modulus(13, 3)

# Menampilkan hasil
print("Hasil penjumlahan:", hasil_penjumlahan)
print("Hasil pengurangan:", hasil_pengurangan)
print("Hasil perkalian:", hasil_perkalian)
print("Hasil pembagian:", hasil_pembagian)
print("Hasil perpangkatan:", hasil_perpangkatan)
print("Hasil modulus:", hasil_modulus)
