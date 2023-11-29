def balikan(daftar_buah):
    buah_terbalik = []
    panjang_daftar = len(daftar_buah)

    for i in range(panjang_daftar - 1, -1, -1):
        buah_terbalik.append(daftar_buah[i])

    return buah_terbalik

buah_awal = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_terbalik = balikan(buah_awal)
print(hasil_terbalik)