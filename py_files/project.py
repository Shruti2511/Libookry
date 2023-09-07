from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# importing ui
from main_window import Ui_MainWindow
from delete_dialog import Ui_delete_dialog
from edit_dialog import Ui_Dialog as Ui_edit_dialog
from add_dialog import Ui_Dialog as Ui_add_dialog

# import my functions
import my_functions as lib

# edit window
class EditDialog(QDialog):
    def __init__(self, parent = None):
        super(EditDialog, self).__init__(parent)
        self.ui = Ui_edit_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

# add window
class AddDialog(QDialog):
    def __init__(self, parent = None):
        super(AddDialog, self).__init__(parent)
        self.ui = Ui_add_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

# delete window
class DeleteDialog(QDialog):
    def __init__(self, parent = None):
        super(DeleteDialog, self).__init__(parent)
        self.ui = Ui_delete_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

# main window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book_button.pressed.connect(self.show_add_dialog)
        self.load_issued_table()
        self.load_unissued_table()
        self.load_allbooks_table()
        self.edit_button.clicked.connect(lambda: self.edit_book(self.issued_books_table))
        self.edit_button2.clicked.connect(lambda: self.edit_book(self.unissued_books_table))
        
        self.delete_button.clicked.connect(lambda: self.delete_book(self.issued_books_table))
        self.delete_button2.clicked.connect(lambda: self.delete_book(self.unissued_books_table))

        self.refresh_button.clicked.connect(self.load_issued_table)
        self.refresh_button2.clicked.connect(self.load_unissued_table)
        
        self.refresh_button3.clicked.connect(self.load_allbooks_table)

        self.search_button.clicked.connect(self.search_book)

    def save_existing_book(self, ui):
        book = {
            'id': int(ui.id_input.text()),
            'name': ui.name_input.text(),
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': int(ui.page_count_input.text()),
            'issued': ui.yes_button.isChecked(),
            'author': ui.author_input.text(),
            'year': int(ui.year_input.text())
        }
        lib.update_book(book)

    def edit_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            book = lib.find_book(book_id)
            # creating edit dialog
            dialog = EditDialog()
            dialog.ui.id_input.setValue(int(book.id))
            dialog.ui.name_input.setText(book.name)
            dialog.ui.description_input.setText(book.description)
            dialog.ui.isbn_input.setText(book.isbn)
            dialog.ui.page_count_input.setValue(int(book.page_count))
            dialog.ui.yes_button.setChecked(book.issued)
            if book.issued == False:
                dialog.ui.no_button.setChecked(True)
            dialog.ui.author_input.setText(book.author)
            dialog.ui.year_input.setValue(int(book.year))

            dialog.ui.buttonBox.accepted.connect(lambda: self.save_existing_book(dialog.ui))
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()

    def save_new_book(self, ui):
        #dictionary to store information
        new_book = {
            'id': int(ui.id_input.text()),
            'name': ui.name_input.text(),
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': int(ui.page_count_input.text()),
            'issued': ui.yes_button.isChecked(),
            'author': ui.author_input.text(),
            'year': int(ui.year_input.text())
        }
        for attr in new_book:
            if new_book[attr] == None or str(new_book[attr]) == "":
                return False
        lib.add_book(new_book)
        self.load_issued_table()
        self.load_unissued_table()

    def search_book(self):
        if self.search_bar.text() != "":
            book = lib.find_book(int(self.search_bar.text()))
            if book != None:
                self.search_table.setRowCount(1)
                book_dict = book.to_dict()
            
            for book_index, attr in enumerate(book_dict):
                self.search_table.setItem(0, book_index, QTableWidgetItem(str(book_dict[str(attr)])))
                self.search_table.item(0, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


    def delete_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            dialog = DeleteDialog()
            dialog.ui.buttonBox.accepted.connect(lambda: lib.delete_book(book_id))
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()
    
    def load_issued_table(self):
        books = lib.get_issued_books()
        self.issued_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.issued_books_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.issued_books_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_unissued_table(self):
        books = lib.get_unissued_books()
        self.unissued_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.unissued_books_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.unissued_books_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_allbooks_table(self):
        books = lib.load_books()
        self.allbooks_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.allbooks_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.allbooks_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    
    def show_add_dialog(self):
        input_dlg = AddDialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
