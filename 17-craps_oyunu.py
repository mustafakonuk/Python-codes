import random

def oyun():
    i = 1
    toplam = 0
    while i<=2:
        zar = random.randint(1,6)
        toplam += zar
        i+=1
    return toplam

zarlar_toplami = oyun() # oyun() fonksiyonunun çıktısını zarlar toplamına atadık.

#7 veya 11 gelirse oyunu kazanır.
if (zarlar_toplami == 7) or (zarlar_toplami == 11) :
    print(zarlar_toplami,"geldi..")
    print("Tebrikler! Oyunu Kazandın..")

#2,3 veya 12 gelirse oyunu kaybeder.
elif (zarlar_toplami == 2) or (zarlar_toplami == 3) or (zarlar_toplami == 12):
    print(zarlar_toplami,"geldi..")
    print("Maalesef! Oyunu Kaybettin..")

#Eğer zarlar toplamı 4,5,6,8,9,10 gelirse oyun devam eder.
elif (zarlar_toplami == 4) or (zarlar_toplami == 5) or (zarlar_toplami == 6) or (zarlar_toplami == 8) or (zarlar_toplami == 9) or (zarlar_toplami == 10):
    oyuna_devam = oyun()

#devam eden oyunda ilk atışta 7 gelirse oyun biter.
    if(oyuna_devam == 7):
        print("İkinci kisimda ilk",oyuna_devam,"geldi..")
        print("Maalesef! Oyunu Kaybettin..")

    elif (oyuna_devam == zarlar_toplami):
        print(oyuna_devam,"geldi..")
        print("Tebrikler! Oyunu Kazandiniz..")

    else:
        print("Yeniden Dene!!")
