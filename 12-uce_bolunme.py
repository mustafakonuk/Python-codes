#girilen sayının uce bolunme durumunu kontrol eder.

def uce_bolunme(girilen_sayi):
    if(girilen_sayi > 0):
        if(girilen_sayi % 3 == 0):
            print('Girilen sayi uce bolunur.')
        else:
            print('Girilen sayi uce bolunmez.')
    else:
        print('Negatif sayi girdiniz!!')

sayi = int(input("Pozitif bir sayi giriniz:"))
uce_bolunme(sayi)
