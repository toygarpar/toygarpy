import sys

from PyQt5 import QtWidgets

from _radiobutton import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)







        self.ui.Tur.setChecked(True)
        self.ui.lise.setChecked(True)





        #ülkeler
        self.ui.Tur.toggled.connect(self.onClickedUlke)
        self.ui.Ger.toggled.connect(self.onClickedUlke)
        self.ui.Fin.toggled.connect(self.onClickedUlke)
        self.ui.Nor.toggled.connect(self.onClickedUlke)




        #eğitim
        self.ui.ilk.toggled.connect(self.onClickedEdu)
        self.ui.lise.toggled.connect(self.onClickedEdu)
        self.ui.uni.toggled.connect(self.onClickedEdu)
        self.ui.mas.toggled.connect(self.onClickedEdu)




        self.ui.btn_ulke.clicked.connect(self.get_selected_ulke)
        self.ui.btn_edu.clicked.connect(self.get_selected_edu)







    def onClickedUlke(self):
        
        rb = self.sender()

        if rb.isChecked():
            print("Yapılan Seçim: " + rb.text())



    def get_selected_ulke(self):

        ulkeler = self.ui.groupUlke.findChildren(QtWidgets.QRadioButton)

        for rb in ulkeler:
            if rb.isChecked():
                self.ui.lbl_ulke.setText("Seçilen Ülke: " + rb.text())


    def onClickedEdu(self):
        
        rb = self.sender()

        if rb.isChecked():
            print("Yapılan Seçim: " + rb.text())


    def get_selected_edu(self):

        kurumlar = self.ui.groupEdu.findChildren(QtWidgets.QRadioButton)

        for rb in kurumlar:
            if rb.isChecked():
                self.ui.lbl_edu.setText("Seçilen Eğitim: " + rb.text())


















def app():

    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QtWidgets.QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = Window()

    #displays the window on the screen
    win.show()  # Show the window

    # sys.exit() ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop, app.exec_() runs the event loop until the application is closed





app()