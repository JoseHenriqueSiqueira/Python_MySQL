import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
sys.path.append(r'./src')
from Base import BaseDAO
import threading

class Database(QObject):
    data_ready = pyqtSignal(list)

    def get_gerentes(self):
        data = BaseDAO()._execQUERY("SELECT nome, cpf, rg FROM gerentes")
        self.data_ready.emit(data)

class GerentesWindow(QMainWindow):
    def __init__(self, main = None):
        super().__init__(main)
        self.database = Database()
        self.__initUI()

    def __initUI(self):
        self.resize(640, 420)
        self.setWindowTitle('Gerentes')
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.btnAdd = QPushButton('Adicionar', self)
        self.btnAdd.move(self.width() - self.btnAdd.width() - 10, 10)
        self.btnAdd.setFixedWidth(100)
        self.btnAdd.clicked.connect(self.add_gerente)

        self.inputName = QLineEdit(self)
        self.inputName.move(20, 50)
        self.inputName.setFixedWidth(150)
        self.inputName.setFixedHeight(20)

        self.__init_table()

    def __init_table(self):
        threading.Thread(target = self.database.get_gerentes).start()
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addSpacerItem(QSpacerItem(0, 210))

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Nome", "CPF", "RG"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.table)

        self.database.data_ready.connect(self.__insert_data)

    def __insert_data(self, data):
        self.table.setRowCount(len(data))

        for row, (name, cpf, rg) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(cpf))
            self.table.setItem(row, 2, QTableWidgetItem(rg))

    def add_gerente(self):
        print('ok')

    def closeEvent(self, event):
        self.close()

    def resizeEvent(self, event):
        self.btnAdd.move(self.width() - self.btnAdd.width() - 10, 10)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.__initUI()

    def __initUI(self):
        self.resize(1280, 720)
        self.setWindowTitle('Livraria')
        self.setWindowIcon(QIcon('src/Livraria/icons/main.png'))

        stylesheet = """
            MainWindow {
                background-image: url("src/Livraria/icons/background.jpg"); 
            }
        """
        self.setStyleSheet(stylesheet)

        self.__create_menu() # Menu principal

    def __create_menu(self):
        menu_bar = self.menuBar()
        main_menu = menu_bar.addMenu('&Menu')

        actions_data = [
            ('Gerentes', 'src/Livraria/icons/gerentes.png', 'gerentes'),
            ('Leitores', 'src/Livraria/icons/leitores.png', 'leitores'),
            ('Livros', 'src/Livraria/icons/livros.png', 'livros'),
            ('Emprestimos', 'src/Livraria/icons/emprestimos.png', 'emprestimos')
        ]

        for title, path, method in actions_data:
            action = QAction(QIcon(path), f"&{title}", self)
            main_menu.addAction(action)
            action.triggered.connect(getattr(self, method))

    def gerentes(self):
        GerentesWindow(self).show()

    def leitores(self):
        print('leitores')

    def livros(self):
        print('livros')

    def emprestimos(self):
        print('emprestimo')

    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())