kaynak = "ıöüşğ" #Türkçe karakterler.
hedef = "iousg"  #ingilizcede karşılıkları.

ceviri_tablosu = str.maketrans(kaynak,hedef)

metin = """Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir
           programlama dilidir girintilere dayalı basit sözdizimi, dilin öğrenilmesini ve akılda kalmasını
           kolaylaştırır.Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya
           başlanabilen bir dil olma özelliği kazandırır."""

print(metin.translate(ceviri_tablosu)) #türkçe karakterleri ingilizce karakterlere çevirir.
print(metin.lower()) #bütün harfleri küçük harfe dönüştürür.
print(metin.upper()) #bütün hafleri büyük harfe donüştürür.
print(metin.replace("a","A")) #bütün a harfini A harfine dönüştürür.
