# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

#Kullanıcı ismi ve Parola kontrolü programı

kullanici_adi = "ktuceng"
parola = "12345"

girilen_kullanici_adi = input("Kullanici Adi:")
girilen_parola = input("Parola:")

if ((kullanici_adi == girilen_kullanici_adi) and (parola == girilen_parola)):
    print("Bu Siteye Hoşgeldiniz.")
elif ((kullanici_adi != girilen_kullanici_adi) and (parola == girilen_parola)):
    print("Kullanici Adını Yanlış Girdiniz!")
elif ((kullanici_adi == girilen_kullanici_adi) and (parola != girilen_parola)):
    print("Şifrenizimi Unuttunuz?")
else:
    print("Tekrar Deneyin!")
