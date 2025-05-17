import sys

from PyQt5 import QtWidgets

from _datetime import Ui_MainWindow

from PyQt5.QtCore import QDate, QTime, QDateTime







class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




        self.ui.btn_calc_time.clicked.connect(self.calc_time)
        self.ui.btn_calc_date.clicked.connect(self.calc_date)









    def calc_time(self):

        start = self.ui.time_start.time()
        end = self.ui.time_finish.time()
        print(start, end)


        



    def calc_date(self):

        start_date = self.ui.date_start.date()
        end_date  = self.ui.date_finish.date()
        print(start_date, end_date)

        print("Days in month: {0}".format(start_date.daysInMonth()))
        print("Days in year: {0}".format(start_date.daysInYear()))

        print("Total Days: {0}".format(start_date.daysTo(end_date)))

        now = QDate.currentDate()

        print("total days from now: {0}".format(start_date.daysTo(now)))

























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