#kenarların durumlarına göre ucgenin cesidini basar.

def ucgen_cesitleri(kenar1,kenar2,kenar3):
    if(pow(kenar1,2) == pow(kenar2,2) + pow(kenar3,2)):
        print("Dik acili ucgen")
    elif(pow(kenar1,2) > pow(kenar2,2) + pow(kenar3,2)):
        print("Genis acili ucgen")
    elif(pow(kenar1,2) < pow(kenar2,2) + pow(kenar3,2)):
        print("Dar acili ucgen")
    elif (kenar1 >= kenar2 + kenar3):
        print("Ucgen olusmaz!!")

en_uzun     = int(input("En uzun kenar:"))
diger_sayi1 = int(input("Diger kenar:"))
diger_sayi2 = int(input("Diger kenar:"))

if(diger_sayi1 > en_uzun) or (diger_sayi2 > en_uzun):
    print("Lutfen en uzun kenari giriniz")

print(ucgen_cesitleri(en_uzun,diger_sayi1,diger_sayi2))
