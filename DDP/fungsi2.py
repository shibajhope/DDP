def duplikasi(daftar_buah):
    buah_terduplikasi = []

    for buah in daftar_buah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)

    return buah_terduplikasi

buah_awal = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_terduplikasi = duplikasi(buah_awal)
print(hasil_terduplikasi)