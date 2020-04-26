# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

import sqlite3

con = sqlite3.connect("ogrenci_bilgisi.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,numara INT)")
    con.commit()
    con.close()

tablo_olustur()
