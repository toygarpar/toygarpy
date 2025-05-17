import sys

from PyQt5 import QtWidgets


from PyQt5.QtWidgets import QTableWidgetItem

from _table import Ui_MainWindow









class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.load_products()
        self.ui.btn_save.clicked.connect(self.save_product)

        self.ui.products_table.doubleClicked.connect(self.double_clicked)



    def double_clicked(self):

        for p in self.ui.products_table.selectedItems():
            print(p.row(), p.column(), p.text())





    def save_product(self):

        product_name = self.ui.lineEdit_ProductName.text()
        product_price = self.ui.lineEdit_Price.text()


        if product_name and product_price is not None:
            row_count = self.ui.products_table.rowCount()
            print(row_count)
            self.ui.products_table.insertRow(row_count)
            self.ui.products_table.setItem(row_count,0, QTableWidgetItem(product_name) )
            self.ui.products_table.setItem(row_count,1, QTableWidgetItem(str(product_price)) )









    def load_products(self):

        monitors = [
            {"ProductName": "LG 32inch Monitor", "Price": 10000},
            {"ProductName": "LG 34inch Curved Monitor", "Price": 12000},
            {"ProductName": "Viewsonic 32inch Monitor", "Price": 16000},
            {"ProductName": "MSI 32inch Monitor", "Price": 13000}

        ]




        # self.ui.products_table.setRowCount(len(monitors))
        self.ui.products_table.setRowCount(len(monitors))

        self.ui.products_table.setColumnCount(2)

        #set column headers and widths
        self.ui.products_table.setHorizontalHeaderLabels(("ProductName", "Price"))
        self.ui.products_table.setColumnWidth(0,220)
        self.ui.products_table.setColumnWidth(1,110)


        #add monitors to the table
        row_index = 0
        for mon in monitors:
            self.ui.products_table.setItem(row_index,0, QTableWidgetItem(mon["ProductName"]) )
            self.ui.products_table.setItem(row_index,1, QTableWidgetItem(str(mon["Price"])) )

            row_index += 1




        # self.ui.products_table.setItem(0,0, QTableWidgetItem("Samsung 34inch Curved Monitor") )
        # self.ui.products_table.setItem(0,1, QTableWidgetItem("18000") )

        # self.ui.products_table.setItem(1,0, QTableWidgetItem("MSI 40inch Monitor") )
        # self.ui.products_table.setItem(1,1, QTableWidgetItem("15000") )


        # self.ui.products_table.setItem(2,0, QTableWidgetItem("Samsung 32inch Monitor") )
        # self.ui.products_table.setItem(2,1, QTableWidgetItem("13000") )























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