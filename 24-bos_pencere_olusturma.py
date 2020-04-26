from PyQt5.QtWidgets import *
import sys

class YeniPencere(QMainWindow):
    def __init__(self):
        super(YeniPencere, self).__init__()

uygulama = QApplication(sys.argv)
pencere = YeniPencere() #pencere oluşturduk.
pencere.show() #oluşan pencereyi ekranda gösterdik
uygulama.exec_() #pencere oluştu ama hemen açılıp kapanıyodu onu önledik.

#pencere oluşturmak için farklı sınıflar kullanılabilir.
# Bunlar:
# 1-QWidget
# 2-QDialog
# 3-QMainWindow
