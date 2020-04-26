#girilen sayıdan 0'a kadar 5er 5er geriye doğru sayar.

def geriye_sayma(sayi):
    while sayi >= 0:
        print(sayi)
        sayi-=5

girilen_sayi = int(input("Bir sayi giriniz:"))
geriye_sayma(girilen_sayi)
