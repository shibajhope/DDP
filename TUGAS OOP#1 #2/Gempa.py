class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa di", self.lokasi, "tidak berasa.")
        elif 2 <= self.skala < 4:
            print("Dampak gempa di", self.lokasi, "bangunan retak-retak.")
        elif 4 <= self.skala < 6:
            print("Dampak gempa di", self.lokasi, "bangunan roboh.")
        else:
            print("Dampak gempa di", self.lokasi, "bangunan roboh dan berpotensi tsunami.")

# Contoh penggunaan
lokasi_gempa = "Jawa Tengah"
skala_gempa = 6.5
gempa_jateng = Gempa(lokasi_gempa, skala_gempa)
gempa_jateng.dampak()
