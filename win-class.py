#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:52:59 2024

@author: toygar
"""

import PyQt5

import sys  #uygulamaya komut saturundan argüman göndermek için, allows you to interact with the system

from PyQt5 import QtWidgets

#manages application-wide resources and controls the application's event loop
#provides a framework for building windows in your application, supports menus, toolbars, status bars, and more.

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip  # ore module for PyQt5 GUI elements


from PyQt5.QtGui import QIcon



class MyWindow(QMainWindow):  #ave all the functionality that comes with the QMainWindow class, such as window controls, layout, menus, etc.

    """ 
    configure the window by calling various methods that belong to QMainWindow.
    
    """

    def __init__(self):     
        super(MyWindow, self).__init__()  #ensures that the constructor of the parent class (QMainWindow) is called

        """ 
        By calling super(), you're invoking the __init__() method of the parent class (QMainWindow), which does all the necessary setup for the window, such as preparing the window for display.       
        
        
        """


        self.setWindowTitle("My First App")     #the title bar of the window.
    
        self.setGeometry(200,200,500,500)   #pencerinin boyutu, konumu
        
        self.setWindowIcon(QIcon("icon.png"))
        
        self.setToolTip("my tool tip")

        self.initUI()



    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)    
        self.lbl_name.setText("Adınız: ")    
        self.lbl_name.move(50,30)
        
        
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move (50,70)

        self.lbl_res = QtWidgets.QLabel(self)
        self.lbl_res.resize(300,50)
        #self.lbl_res.setText("Sonuç")
        self.lbl_res.move(150,150)

        
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)


        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)



    def clicked(self):
        #print("Buttona Tıklandı! Name: " + self.txt_name.text() +" , Surname: " + self.txt_surname.text())
        self.lbl_res.setText("Ad: " + self.txt_name.text() + " Soyad: " + self.txt_surname.text())


        


# APPLICATION SETUP

def window():



    #main entry point for a PyQt5 application. It manages resources like event handling, application-wide settings, and GUI widgets.
    app = QApplication(sys.argv)        

    #creates an instance of the MyWindow class, initializes the window with the settings you specified in the constructor (__init__()).
    win = MyWindow()

    #displays the window on the screen
    win.show()  # Show the window

    #ensures that the program exits cleanly when the event loop ends.
    sys.exit(app.exec_())  # Start the event loop





window()
