#Girilen uc sayidan en buyugunu ekrana basar.

def buyuk_sayi_bulma(sayi_1,sayi_2,sayi_3):

    if(sayi_2 > sayi_1) and (sayi_2 > sayi_3):
        print("En buyuk sayi:",sayi_2)
    elif (sayi_3 > sayi_1) and (sayi_3 > sayi_2):
        print("En buyuk sayi:",sayi_3)
    else:
        print("En buyuk sayi:",sayi_1)

sayi1 = int(input("Birinci sayi:"))
sayi2 = int(input("Ikinci sayi:"))
sayi3 = int(input("Ucuncu sayi:"))

buyuk_sayi_bulma(sayi1,sayi2,sayi3)
