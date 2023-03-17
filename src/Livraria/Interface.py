import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle('Livraria')
        self.setWindowIcon(QIcon('src/Livraria/icons/main.png'))
        stylesheet = """
            MainWindow {
                background-image: url("src/Livraria/icons/background.jpg"); 
            }
        """
        self.setStyleSheet(stylesheet)

        menu_gerentes = QAction(QIcon('src/Livraria/icons/gerentes.png'), '&Gerentes', self)
        menu_leitores = QAction(QIcon('src/Livraria/icons/leitores.png'), '&Leitores', self)
        menu_livros = QAction(QIcon('src/Livraria/icons/livros.png'), '&Livros', self)
        menu_emprestimos = QAction(QIcon('src/Livraria/icons/emprestimos.png'), '&Emprestimos', self)

        menubar = self.menuBar()
        menu_principal = menubar.addMenu('&Menu')
        menu_principal.addAction(menu_gerentes)
        menu_principal.addAction(menu_leitores)
        menu_principal.addAction(menu_livros)
        menu_principal.addAction(menu_emprestimos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())