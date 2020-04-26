# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

def kok_bulma(a,b,c): #kok_bulma isimli fonksiyon oluşturduk.

    delta = ((b**2)-4*a*c) #deltayı bulduk.
    if (delta < 0):
        print("Reel kok yok!")
        return

    x1 = (-b - delta**0.5)/(2*a) #kökleri bulduk.
    x2 = (-b + delta**0.5)/(2*a)

    return (x1,x2)

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

sonuc = kok_bulma(a,b,c)
print("Kokler:",sonuc)
