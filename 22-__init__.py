import random

class birinci_cephe():
    def __init__(self,isim,can,saldiri_gucu,mermi_sayisi):
        self.isim = isim
        self.can = can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def ekrana_bas(self):
        print("İsim:",self.isim,"\nCan:",self.can,"\nSaldırı Gücü:",self.saldiri_gucu,"\nMermi Sayısı:",self.mermi_sayisi)

oyuncu = []

i = 0
while i < 10:
    rastgele_can = random.randrange(1,10)
    rastgele_saldiri_gucu = random.randrange(50,100)
    rastgele_mermi_sayisi = random.randrange(5,10)
    yeni_oyuncu = birinci_cephe("Oyuncu" + str(i+1),rastgele_can,rastgele_saldiri_gucu,rastgele_mermi_sayisi)
    oyuncu.append(yeni_oyuncu)

    i+=1

print("Birinci Cephe Oyuncuları")
for i in oyuncu:
    i.ekrana_bas()
    print("*******************")

class ikinci_cephe():
    def __init__(self,isim,can,saldiri_gucu,mermi_sayisi):
        self.isim = isim
        self.can = can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def ekrana_bas(self):
        print("İsim:",self.isim,"\nCan:",self.can,"\nSaldırı Gücü:",self.saldiri_gucu,"\nMermi Sayısı:",self.mermi_sayisi)

oyuncu = []

i = 0
while i < 10:
    rastgele_can = random.randrange(1,10)
    rastgele_saldiri_gucu = random.randrange(50,100)
    rastgele_mermi_sayisi = random.randrange(5,10)
    yeni_oyuncu = ikinci_cephe("Oyuncu" + str(i+1),rastgele_can,rastgele_saldiri_gucu,rastgele_mermi_sayisi)
    oyuncu.append(yeni_oyuncu)

    i+=1
print("İkinci Cephe Oyuncuları")
for i in oyuncu:
    i.ekrana_bas()
    print("*******************")
