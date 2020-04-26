# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

sayi = int(input("Bir sayi giriniz:"))

toplam = 0
deger_1 = 1

while deger_1 <= sayi:
    toplam+=deger_1
    deger_1+=1

print("1'den",sayi,"'e kadar olan sayilarin toplamı:",toplam)

carpim = 1
deger_2 = 1

while deger_2 <= sayi:
    carpim*=deger_2
    deger_2+=1

print("1'den",sayi,"'e kadar olan sayilarin carpimi:",carpim)
