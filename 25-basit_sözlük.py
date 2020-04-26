sözlük =[
        ('book','kitap'),('water','su'),
        ('apple','elma'),('pen','kalem'),
        ('lion','aslan'),('cat','kedi'),
        ('dog','köpek'),('bir','kuş'),
        ('home','ev,yuva'),('duck','ördek')
        ] #sözlük tanımladık ve içine çeşitli kelimeler ekledik.

def kelime_bul(kelime): #istenen kelimenin karşılığınu bulur
    for i in sözlük:
        if i[0] == kelime:
            return i[1]

kelime = input("Bir kelime giriniz:") #kelime istedik.
print("Türkçe karşılığı:",kelime_bul(kelime.lower())) #lower metodu ile bütün harfleri küçük yaptık.
