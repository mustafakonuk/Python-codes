sayi = int(input("Büyük sayi giriniz:"))

# formul ==> s=(1 + 1/n)^n
for i in range(1, sayi):
    e_sayisi = pow((1 + 1 / i), i)

print("e sayisi:", e_sayisi)
