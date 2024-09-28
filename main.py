from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from screens.chooseAdventure import screenChooseAdventure
from screens.playAdventure import screenPlayAdventure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.show()

        self.main_menu = QVBoxLayout()
        btn_new_game = QPushButton("New Game")
        btn_new_game.clicked.connect(self.new_game)

        self.main_menu.addWidget(btn_new_game)

        main_widget = QWidget()
        main_widget.setLayout(self.main_menu)
        self.setCentralWidget(main_widget)

    def new_game(self):
        screen = screenChooseAdventure()
        main_widget = QWidget()
        main_widget.setLayout(screen)
        self.setCentralWidget(main_widget)
        screen.adventure_selected.connect(self.start_new_adventure)

    def start_new_adventure(self, title):
        screen = screenPlayAdventure()
        screen.new_adventure(title)


app = QApplication()
window = MainWindow()
window.show()
app.exec()