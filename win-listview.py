import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

from _listview import Ui_MainWindow









class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()




        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        #loadPlayers
        self.load_players()

        #add new player
        self.ui.btn_add.clicked.connect(self.add_player)

        #edit player
        self.ui.btn_edit.clicked.connect(self.edit_player)

        #delete player
        self.ui.btn_rm.clicked.connect(self.remove_player)

        #up Player
        self.ui.btn_up.clicked.connect(self.up_player)

        #down player
        self.ui.btn_down.clicked.connect(self.down_player)

        #sort players        
        self.ui.btn_sort.clicked.connect(self.sort_players)

        #exit listview
        self.ui.btn_exit.clicked.connect(self.exit_list)




    def load_players(self):

        self.ui.list_items.addItems(["Zehra Güneş", "Kiera Van Ryk", "Marina Markova"])

        #indekse göre ilk eleman seçili gelsin
        self.ui.list_items.setCurrentRow(0)


    def add_player(self):
        current_index = self.ui.list_items.currentRow()  #giriş yapılacak index, index alma




        text, ok  = QInputDialog.getText(self, "New Player", "Player Name")

        if text and ok is not None:
            # self.ui.list_items.insertItem(0, text)  #indeks ve girilecek text belirlenir
            self.ui.list_items.insertItem(current_index, text)





    def edit_player(self):
        get_index =  self.ui.list_items.currentRow()

        get_player = self.ui.list_items.item(get_index)  #indeks ile oyuncuyu seçmek için



        if get_player is not None:
            edit_name_text , ok = QInputDialog.getText(self, "Edit Player", "Edit Player Name", QLineEdit.Normal, get_player.text())

            if edit_name_text and ok is not None:
                get_player.setText(edit_name_text)


    def remove_player(self):
        get_index =  self.ui.list_items.currentRow()
        get_player = self.ui.list_items.item(get_index)  #indeks ile oyuncuyu seçmek için

        if get_player is None:
            return
        
        Q = QMessageBox.question(self, "Remove Player", "Are you sure to remove the Player, " + get_player.text(), QMessageBox.Yes | QMessageBox.No )


        if Q == QMessageBox.Yes:
            get_player = self.ui.list_items.takeItem(get_index)
            del get_player


    def up_player(self):

        current_index =  self.ui.list_items.currentRow()
        
        
        if current_index > 0:
            current_player = self.ui.list_items.takeItem(current_index)       #indeksi verip elemanı alalım
            self.ui.list_items.insertItem(current_index - 1, current_player)  #oyuncuyu bir yukarı indekse yerleştirelim
            # self.ui.list_items.setCurrentRow(current_index - 1 )
            self.ui.list_items.setCurrentItem(current_player)  #up ve down hareketleri için iki değişik yol koydum


    def down_player(self):
        current_index = self.ui.list_items.currentRow()

        if current_index < self.ui.list_items.count() - 1:  # Ensure we're not at the bottom of the list
            current_item = self.ui.list_items.takeItem(current_index)
            self.ui.list_items.insertItem(current_index + 1, current_item)
            self.ui.list_items.setCurrentRow(current_index + 1)  # Update selection
  


    def sort_players(self):
        self.ui.list_items.sortItems()


    def exit_list(self):
        quit()


























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