#PyQt5 UI Calculator Application

from PyQt5 import QtWidgets

import sys

from UIcalculator import Ui_calculator



class CalcApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(CalcApp, self).__init__()
        self.ui = Ui_calculator()
        self.ui.setupUi(self)
        self.ui.btn_add.clicked.connect(self.calc)
        self.ui.btn_sub.clicked.connect(self.calc)
        self.ui.btn_mul.clicked.connect(self.calc)
        self.ui.btn_div.clicked.connect(self.calc)











    def calc(self):   
        sender = self.sender().text() #hangi butona tıklandığını anlamak için

        result = 0
        if sender == "Topla":
            result =  int(self.ui.txt_num1.text()) + int(self.ui.txt_num2.text())
        elif sender == "Çıkar":
            result =  int(self.ui.txt_num1.text()) - int(self.ui.txt_num2.text())
        elif sender == "Çarp":
            result =  int(self.ui.txt_num1.text()) * int(self.ui.txt_num2.text())
        elif sender == "Böl":
            result =  int(self.ui.txt_num1.text()) / int(self.ui.txt_num2.text())


        self.ui.lbl_res.setText("Sonuç: " + str(result))


def app():

    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QtWidgets.QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = CalcApp()

    #displays the window on the screen
    win.show()  # Show the window

    #ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop





app()