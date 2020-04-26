#belirli bir durumu sorgulama yapmaya örnek.

print("Patirmasiyla meshur ilimiz hangisidir?")
print("...UC HAKKINIZ VAR...")

girilen_il = ''
i=1
while i<=3:
    print(i,".sans")
    girilen_il = input("Bir il giriniz:")
    if girilen_il == "kayseri":
        print("Tebrikler! Pastirmasi ile meshur ilimiz Kayseridir.")
        break
    i+=1
else:
    print("Butun haklarinizi kullandiniz..")
