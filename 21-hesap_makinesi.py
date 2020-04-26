class hesap_makinesi:
    def toplama(sayi1,sayi2):
        return sayi1 + sayi2

    def cikarma(sayi1,sayi2):
        return sayi1 - sayi2

    def carpma(sayi1,sayi2):
        return sayi1 * sayi2

    def bolme(sayi1,sayi2):
        if sayi1 >= sayi2:
            return sayi1 / sayi2
        else:
            return sayi2 / sayi1

print("YAPACAGINIZ İSLEMİN İSARETİNİ GİRİNİZ(+,-,*,/)")
islem = input("Yapilacak islem::")

girilen_sayi1 = int(input("Birinci sayi:"))
girilen_sayi2 = int(input("Ikinci sayi:"))

if islem == "+":
    print("Sonuc:",hesap_makinesi.toplama(girilen_sayi1,girilen_sayi2))
elif islem == "-":
    print("Sonuc:",hesap_makinesi.cikarma(girilen_sayi1,girilen_sayi2))
elif islem == "*":
    print("Sonuc:",hesap_makinesi.carpma(girilen_sayi1,girilen_sayi2))
elif islem == "/":
    print("Sonuc:",hesap_makinesi.bolme(girilen_sayi1,girilen_sayi2))
else:
    print("Lutfen dört islemden birini seciniz!!")
