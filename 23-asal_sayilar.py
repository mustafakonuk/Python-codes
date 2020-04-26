def asal_sayilar(sayi): #asal sayilari bulur.
    for i in range(2,sayi):
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            print(i,"sayisi asal.")

print("Kaça kadar ki asal sayıları bulalım??")
sayi = int(input("Bir sayi giriniz:"))

asal_sayilar(sayi)
