import sys

from PyQt5 import QtWidgets

from _checkboxForm import Ui_MainWindow



class FavoriApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FavoriApp, self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        #teams
        self.ui.cbVkf.stateChanged.connect(self.show_state)
        self.ui.cbEcz.stateChanged.connect(self.show_state)
        self.ui.cbFB.stateChanged.connect(self.show_state)


        self.ui.btnFavori.clicked.connect(self.getAllTeams)


        #langs
        self.ui.cbGo.stateChanged.connect(self.show_state)
        self.ui.cbPy.stateChanged.connect(self.show_state)
        self.ui.cbRust.stateChanged.connect(self.show_state)


        self.ui.btnDilFavori.clicked.connect(self.getAllLangs)


    def getAllTeams(self):
        result = ""
        items = self.ui.groupTeams.findChildren(QtWidgets.QCheckBox)
        print(items)

        for cb in items:
            if cb.isChecked():
                # print(cb.text())
                # print(cb.isChecked())
                result += cb.text() + "\n"
        
        self.ui.lbl_resteams.setText("Favori Takımlar: \n" + str(result))


    def getAllLangs(self):
        result = ""
        items = self.ui.groupLangs.findChildren(QtWidgets.QCheckBox)
        print(items)

        for cb in items:
            if cb.isChecked():
                # print(cb.text())
                # print(cb.isChecked())
                result += cb.text() + "\n"
        
        self.ui.lbl_reslangs.setText("Favori Diller: \n" + str(result))


    def show_state(self,value):
        
        cb = self.sender()

        print(cb)
        print(value)
        print(cb.text())
        print(cb.isChecked())
        
        
        # print(value)
        # print(self.ui.cbVkf.isChecked())
        # print(self.ui.cbVkf.text())


        # self.ui.lbl_res.setText("Sonuç: " + str(result))

















def app():

    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QtWidgets.QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = FavoriApp()

    #displays the window on the screen
    win.show()  # Show the window

    # sys.exit() ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop, app.exec_() runs the event loop until the application is closed





app()