class Hewan:
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.cara_berkembang_biak = cara_berkembang_biak

class Kucing(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, warna_bulu, perilaku):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)
        self.warna_bulu = warna_bulu
        self.perilaku = perilaku

    def bersuara(self):
        return "Meong"

    def berscratch(self):
        return f"{self.nama} sedang melakukan scratching."

class Monyet(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, panjang_ekor, tingkat_kecerdasan):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)
        self.panjang_ekor = panjang_ekor
        self.tingkat_kecerdasan = tingkat_kecerdasan

    def bersuara(self):
        return "Ook ook aah aah"

    def bergelantungan(self):
        return f"{self.nama} sedang bergelantungan di ranting."

class KupuKupu(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, warna_sayap, pola_sayap):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)
        self.warna_sayap = warna_sayap
        self.pola_sayap = pola_sayap

    def terbang(self):
        return f"{self.nama} sedang terbang dengan anggun."

    def menghisap_nektar(self):
        return f"{self.nama} sedang menghisap nektar dari bunga."

# Contoh penggunaan:
kucing = Kucing("Meong", "Ikan", "Rumah", "Melahirkan", "Oren", "Ramah")
monyet = Monyet("Ook", "Buah", "Hutan", "Melahirkan", "Panjang", "Tinggi")
kupu_kupu = KupuKupu("Kupu", "Nektar", "Taman", "Telur", "Warna-warni", "Polkadot")

print(kucing.bersuara())
print(kucing.berscratch())

print(monyet.bersuara())
print(monyet.bergelantungan())

print(kupu_kupu.terbang())
print(kupu_kupu.menghisap_nektar())

