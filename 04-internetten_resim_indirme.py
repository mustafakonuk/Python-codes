# -------------------------------#
# Mustafa Konuk                  #
# Karadeniz Teknik Üniversitesi  #
# mustafakonuk@outlook.com.tr    #
#                                #
# -------------------------------#

import urllib.request

url1 = "https://wall.alphacoders.com/big.php?i=717747"
url2 = "https://wall.alphacoders.com/big.php?i=84436"
url3 = "https://wall.alphacoders.com/big.php?i=89290"

url_listesi = [url1,url2,url3]
say = 1

for url in url_listesi:
    urllib.request.urlretrieve(url,"Resim" + str(say)+".jpg")
    say+=1
