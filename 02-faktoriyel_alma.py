# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

sayi = int(input("Bir sayi giriniz:"))

faktoriyel = 1
for i in range(1,sayi + 1):
    faktoriyel = faktoriyel*i
print("Girilen sayinin faktoriyeli:",faktoriyel)
