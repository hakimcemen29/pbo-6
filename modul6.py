import math

class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi ** 2

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari ** 2

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma

    def luas(self):
        return self.alas * self.tinggi_alas + 3 * self.alas * self.tinggi_prisma

    def volume(self):
        return (1/2) * self.alas * self.tinggi_alas * self.tinggi_prisma

def main():
    kubus = Kubus(5)
    balok = Balok(4, 3, 6)
    bola = Bola(7)
    tabung = Tabung(4, 8)
    prisma_segitiga = PrismaSegitiga(6, 8, 10)

    print("Luas dan Volume 5 Bangun Ruang:")
    print("Kubus - Luas:", kubus.luas(), ", Volume:", kubus.volume())
    print("Balok - Luas:", balok.luas(), ", Volume:", balok.volume())
    print("Bola - Luas:", bola.luas(), ", Volume:", bola.volume())
    print("Tabung - Luas:", tabung.luas(), ", Volume:", tabung.volume())
    print("Prisma Segitiga - Luas:", prisma_segitiga.luas(), ", Volume:", prisma_segitiga.volume())

if __name__ == "__main__":
    main()
