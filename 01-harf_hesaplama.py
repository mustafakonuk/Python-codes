   
   # -------------------------------#
   # Mustafa Konuk                  #
   # Karadeniz Teknik Üniversitesi  #
   # mustafakonuk@outlook.com.tr    #
   #                                #
   # -------------------------------#
   
vize = int(input("Vize notunuzu giriniz:")) 
final = int(input("Final notunuzu giriniz:"))

ortalama = (vize/2) + (final/2)

if ortalama >=85:
    print("Harfli notunuz: AA")
    print("Ortalamaniz:",ortalama)
elif ortalama >=70:
    print("Harfli notunuz: BB")
    print("Ortalamaniz:", ortalama)
elif ortalama >=45:
    print("Harfli notunuz: CC")
    print("Ortalamaniz:", ortalama)
elif ortalama >=1:
    print("Harfli notunuz: FF")
    print("Ortalamaniz:", ortalama)
else:
    print("Lütfen pozitif bir sayi giriniz!")
