from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from screens.chooseAdventure import screenChooseAdventure
from screens.playAdventure import screenPlayAdventure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.show()

        self.change_screen(self.screen_main_menu())

    def screen_main_menu(self):
        main_menu = QVBoxLayout()
        btn_new_game = QPushButton("New Game")
        btn_new_game.clicked.connect(self.new_game)
        main_menu.addWidget(btn_new_game)
        return main_menu

    def new_game(self):
        screen = screenChooseAdventure()
        self.change_screen(screen)
        screen.adventure_selected.connect(self.start_new_adventure)

    def start_new_adventure(self, title):
        screen = screenPlayAdventure()
        screen.sig_main_menu.connect(self.return_to_main_menu)
        self.change_screen(screen)
        screen.new_adventure(title)

    def change_screen(self, screen):
        main_widget = QWidget()
        main_widget.setLayout(screen)
        self.setCentralWidget(main_widget)

    def return_to_main_menu(self):
        self.change_screen(self.screen_main_menu())


app = QApplication()
window = MainWindow()
window.show()
app.exec()
