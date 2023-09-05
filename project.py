from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# importing ui
from main_window import Ui_MainWindow
from delete_dialog import Ui_delete_dialog
from edit_dialog import Ui_Dialog as Ui_edit_dialog
from add_dialog import Ui_Dialog as Ui_add_dialog
#import my functions
import my_functions as lib

# main window
class AddDialog(QDialog):
    def __init__(self, parent=None):
        super(AddDialog, self).__init__(parent)
        self.ui = Ui_add_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book_button.pressed.connect(self.show_add_dialog)

    def save_new_book(self, ui):
        #dictionary to store information
        new_book = {
            'id': int(ui.id_input.text()),
            'name': ui.name_input.text(),
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': int(ui.page_count_input.text()),
            'issued': ui.yes.isChecked(),
            'author': ui.author_input.text(),
            'year': int(ui.year_input.text())
        }
    
    def show_add_dialog(self):
        input_dlg = AddDialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
