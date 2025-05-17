import sys

from PyQt5 import QtWidgets

from _combobox import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # self.ui.cbCities.addItem("Ankara")
        # self.ui.cbCities.addItem("İstanbul")
        # self.ui.cbCities.addItem("İzmir")
        # self.ui.cbCities.addItem("Bursa")


        combo = self.ui.cbCities


        combo.addItem("Ankara")
        combo.addItem("İstanbul")
        combo.addItem("İzmir")
        combo.addItem("Bursa")
        #combo.addItems(["Karabük", "Giresun", "Çorum"])




        self.ui.btn_loaditems.clicked.connect(self.load_items)
        self.ui.btn_getitem.clicked.connect(self.get_item)
        self.ui.btn_clearitems.clicked.connect(self.clear_items)


        
        self.ui.cbCities.currentIndexChanged.connect(self.sel_changed_index)
        self.ui.cbCities.currentIndexChanged[str].connect(self.sel_changed_text)

        



    def load_items(self):

        cities = ["Karabük", "Giresun", "Çorum"]

        self.ui.cbCities.addItems(cities)





    def get_item(self):

        print(self.ui.cbCities.currentText())
        print(self.ui.cbCities.currentIndex())
        
        
        count = self.ui.cbCities.count()
        for c in range(count):
            print(self.ui.cbCities.itemText(c))

        
        
        #get item tıklandığında qlabela index ve city yazılsın!
        self.ui.groupCities.findChildren(QtWidgets.QComboBox)

        self.ui.lbl_res.setText("Seçilen Şehir: \n" + self.ui.cbCities.currentText() + "\n" + str(self.ui.cbCities.currentIndex()))



    def clear_items(self):

        self.ui.cbCities.clear()





    def sel_changed_index(self,index):
        
        print(index)


    def sel_changed_text(self,text):

        print(text)

































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