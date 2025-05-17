import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QMessageBox

from _msgbox import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.ui.btn_exit.clicked.connect(self.show_dialog)




    def show_dialog(self):

        result = QMessageBox.question(self, "Close App", "Are you sure", QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore , QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print("Okay clicked!")
            QtWidgets.qApp.quit()

        else:
            print("Okay Not Clicked, Stay in the Program!")


        #alternatif uzun yolu

    #     msg = QMessageBox()


    #     msg.setWindowTitle("Close The App")
    #     msg.setText("Are you sure?")
    #     # msg.setIcon(QMessageBox.Question)
    #     msg.setIcon(QMessageBox.Warning)
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)

    #     msg.setDefaultButton(QMessageBox.Ok)
    #     msg.setDetailedText("Details...")
    #     msg.buttonClicked.connect(self.popup_button)

    






    #     x = msg.exec()
    #     print(x)


   
    

    # def popup_button(self, obj):
    #     #print(obj.text())



    #     text = obj.text().replace("&", "")  # Remove the ampersand
    #     if text == "OK":
    #         print("Okay...")
    #         QtWidgets.qApp.quit()


    #     elif text == "Cancel":
    #         print("Cancel...")
    #     else:
    #         print("Ignore...")
















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