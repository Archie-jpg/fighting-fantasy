from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel


class QShop(QWidget):
    sig_buy_item = Signal(str, int)
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

    def create_shop(self, data, gold):
        for item in data:
            new_item = ShopItem(item, data[item])
            if new_item.price > gold:
                new_item.btnBuy.setVisible(False)
            new_item.btnBuy.clicked.connect(self.buy_item)
            self.layout().addWidget(new_item)

    def buy_item(self):
        self.sig_buy_item.emit(self.sender().parent().name, self.sender().parent().price)
        self.sender().parent().set_sold()


class ShopItem(QWidget):
    def __init__(self, name, price):
        super().__init__()
        # Variable
        self.name = name
        self.price = int(price)
        # Widgets
        self.lblName = QLabel(name)
        self.lblPrice = QLabel(f"{price} gold")
        self.btnBuy = QPushButton("Buy")
        # Layout
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.lblName)
        self.layout().addWidget(self.lblPrice)
        self.layout().addWidget(self.btnBuy)

    def set_sold(self):
        self.btnBuy.setVisible(False)
        self.lblName.setText("Sold")
        self.lblPrice.setText("")
