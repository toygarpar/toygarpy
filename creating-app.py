import PyQt5

import sys  #uygulamaya komut saturundan argüman göndermek için

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip

from PyQt5.QtGui import QIcon




def window():
    app = QApplication(sys.argv)
    win = QMainWindow()



    win.setWindowTitle("My First App")
    
    win.setGeometry(200,200,500,500)   #pencerinin boyutu, konumu
    
    win.setWindowIcon(QIcon("icon.png"))
    
    win.setToolTip("my tool tip")
    
    
    
    
    
    
    
    
    
    
    

    win.show()
    sys.exit(app.exec_())



window()