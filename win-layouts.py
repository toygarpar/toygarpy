import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow    #Contains classes for creating GUI applications
from PyQt5.QtGui import QPalette, QColor    #Provides tools for managing color (QColor) and palette settings (QPalette


class Color(QWidget):           #subclass of QWidget, used to display a colored widget
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  #Ensures that the background color of the widget is filled when displayed.


        palette = self.palette()   #Retrieves the current color palette of the widget.
        palette.setColor(QPalette.Window, QColor(color))   #Sets the window (background) color of the widget using the specified color
        self.setPalette(palette)    #applies the modified palette to the widget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)



        # layout = QtWidgets.QVBoxLayout()   #vertical
        layout = QtWidgets.QHBoxLayout()    #horizantal


        layout.addWidget(Color("red"))
        layout.addWidget(Color("white"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))




        widget = QWidget()
        widget.setLayout(layout)







        #widget = Color("blue")          #Creates an instance of the Color class with a blue background.
        self.setCentralWidget(widget)   #Embeds the Color widget into the main window's central area









def app():

    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = MainWindow()

    #displays the window on the screen
    win.show()  # Show the window

    # sys.exit() ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop, app.exec_() runs the event loop until the application is closed





app()