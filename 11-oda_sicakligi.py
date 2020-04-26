#girilen dereceye göre odanın durumunu belirtir.

def oda_sicakligi(girilen):
    if girilen < 22:
        print("Soğuk Odalar..!")
    elif (girilen >=22) and (girilen <=25):
        print("Oda ideal Sicaklikta!!")
    else:
        print("Oda Cok Sicak!!!")

oda_derece = input("Oda sicakligini giriniz:")
oda_derece = float(oda_derece)
oda_sicakligi(oda_derece)
