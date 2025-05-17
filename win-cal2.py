import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow





class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()


        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initGUI()
        

    def initGUI(self):

        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Sayı 1: ")
        self.lbl_num1.move(50,30)

        self.txt_num1 = QtWidgets.QLineEdit(self)        
        self.txt_num1.move(150,30)
        self.txt_num1.resize(200,32)



        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Sayı 2: ")
        self.lbl_num2.move(50,80)

        self.txt_num2 = QtWidgets.QLineEdit(self)        
        self.txt_num2.move(150,80)
        self.txt_num2.resize(200,32)



        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Topla=>")
        self.btn_add.move(150,130)
        self.btn_add.clicked.connect(self.calc)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("Çıkar=>")
        self.btn_sub.move(150,170)
        self.btn_sub.clicked.connect(self.calc)

        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText("Çarp=>")
        self.btn_mul.move(150,210)
        self.btn_mul.clicked.connect(self.calc)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Böl=>")
        self.btn_div.move(150,250)
        self.btn_mul.clicked.connect(self.calc)




        self.lbl_res = QtWidgets.QLabel(self)
        self.lbl_res.setText("Sonuç: ")
        self.lbl_res.move(150,290)





    # def add(self):
    #     result =  int(self.txt_num1.text()) + int(self.txt_num2.text())
    #     self.lbl_res.setText("Sonuç: " + str(result))

    # def sub(self):
    #     result =  int(self.txt_num1.text()) - int(self.txt_num2.text())
    #     self.lbl_res.setText("Sonuç: " + str(result))

    # def mul(self):
    #     result =  int(self.txt_num1.text()) * int(self.txt_num2.text())
    #     self.lbl_res.setText("Sonuç: " + str(result))

    # def div(self):
    #     result =  int(self.txt_num1.text()) / int(self.txt_num2.text())
    #     self.lbl_res.setText("Sonuç: " + str(result))

    result = 0


    def calc(self):   
        sender = self.sender().text() #hangi butona tıklandığını anlamak için

        result = 0
        if sender == "Topla=>":
            result =  int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == "Çıkar=>":
            result =  int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == "Çarp=>":
            result =  int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == "Böl=>":
            result =  int(self.txt_num1.text()) / int(self.txt_num2.text())


        self.lbl_res.setText("Sonuç: " + str(result))






        # print(sender.text())


        # result =  int(self.txt_num1.text()) / int(self.txt_num2.text())
        # self.lbl_res.setText("Sonuç: " + str(result))


def app():

    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = MainForm()

    #displays the window on the screen
    win.show()  # Show the window

    #ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop





app()
        