# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#
def faktoriyel_alma(sayi): #faktoriyel_alma isimli bir fonksiyon oluşturduk.
    faktoriyel = 1
    for i in range(1,sayi + 1):
        faktoriyel = faktoriyel*i
    print("Girilen sayinin faktoriyeli:",faktoriyel)

sayi = int(input("Bir sayi giriniz:")) #dışardan bir sayi aldık.
faktoriyel_alma(sayi) #fonksiyonumuzu çağırdık.
