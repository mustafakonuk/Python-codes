komsu_iller = ["yozgat","sivas","kahramanmaras","adana","niğde","nevşehir"]

print("Kayseriye Komşu İller...")
girilen_il = input("Bir il giriniz:")

i = 0
#lower metodu ile büyük-küçük harf sorununu ortadan kaldırdık.
while i < len(girilen_il):
    if komsu_iller[i] == girilen_il.lower():
        print(girilen_il.capitalize(),",Kayseri iline komsu!")
        break
    i+=1
#capitalize() metodu ile girilen ilin ilk harfini büyük bastırdık.
else:
    print(girilen_il.capitalize(),",Kayseri iline komsu degil!!")
