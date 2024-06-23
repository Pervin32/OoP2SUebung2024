from PyQt6.QtWidgets import QWidget, QPushButton, QTextBrowser, QLabel, QGridLayout, QRadioButton, QCheckBox, QLineEdit
from PyQt6.QtCore import Qt, pyqtSlot
import sys


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        self.pizza_size = QLabel("Pizzagröße:")
        layout.addWidget(self.pizza_size, 1, 1)

        self.pizza_small = QRadioButton("Kleine Pizza")
        self.pizza_small.clicked.connect(self.choose_pizza_size)
        layout.addWidget(self.pizza_small, 2, 1)
        self.pizza_normal = QRadioButton("Normale Pizza")
        self.pizza_normal.clicked.connect(self.choose_pizza_size)
        layout.addWidget(self.pizza_normal, 3, 1)
        self.pizza_family = QRadioButton("Familien Pizza")
        self.pizza_family.clicked.connect(self.choose_pizza_size)
        layout.addWidget(self.pizza_family, 4, 1)

        self.pizza_topings = QLabel("Pizzabelag:")
        layout.addWidget(self.pizza_topings, 5, 1)

        salami = QCheckBox("Salami")
        salami.clicked.connect(self.add_text)
        layout.addWidget(salami, 6, 1)
        schinken = QCheckBox("Schinken")
        schinken.clicked.connect(self.add_text)
        layout.addWidget(schinken, 6, 2)
        ananas = QCheckBox("Ananas")
        ananas.clicked.connect(self.add_text)
        layout.addWidget(ananas, 7, 1)
        rukola = QCheckBox("Rukola")
        rukola.clicked.connect(self.add_text)
        layout.addWidget(rukola, 7, 2)
        oliven = QCheckBox("Oliven")
        oliven.clicked.connect(self.add_text)
        layout.addWidget(oliven, 8, 1)
        tunfisch = QCheckBox("Tunfisch")
        tunfisch.clicked.connect(self.add_text)
        layout.addWidget(tunfisch, 8, 2)
        zwiebeln = QCheckBox("Zwiebeln")
        zwiebeln.clicked.connect(self.add_text)
        layout.addWidget(zwiebeln, 9, 1)

        self.drinks = QLabel("Trinken:")
        layout.addWidget(self.drinks, 10, 1)

        self.coke = QPushButton("Cola")
        self.coke.pressed.connect(self.choose_drink)
        layout.addWidget(self.coke, 11, 1)
        self.fanta = QPushButton("Fanta")
        self.fanta.pressed.connect(self.choose_drink)
        layout.addWidget(self.fanta, 11, 2)
        self.sprite = QPushButton("Sprite")
        self.sprite.pressed.connect(self.choose_drink)
        layout.addWidget(self.sprite, 12, 1)
        self.water = QPushButton("Wasser")
        self.water.pressed.connect(self.choose_drink)
        layout.addWidget(self.water, 12, 2)

        self.where_to_eat = QLabel("Wo esssen?")
        layout.addWidget(self.where_to_eat, 13, 1)

        self.eat_hear = QPushButton("Hier essen")
        self.eat_hear.pressed.connect(self.choose_eating_place)
        layout.addWidget(self.eat_hear, 14, 1)
        self.to_go = QPushButton("To go")
        self.to_go.pressed.connect(self.choose_eating_place)
        layout.addWidget(self.to_go, 14, 2)

        info = QLabel("Info:")
        layout.addWidget(info, 15, 1)

        self.text_browser = QTextBrowser()
        self.text_browser.setText(self.pizza_size.text() + "\n")
        layout.addWidget(self.text_browser, 16, 1, 1, 2)

        card_info = QLabel("Karteninfos:")
        layout.addWidget(card_info, 17, 1)

        card_holder = QLabel("Karteninhaben:")
        card_holder.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(card_holder, 18, 1)

        name_input = QLineEdit()
        layout.addWidget(name_input, 18, 2)

        iban = QLabel("IBAN:")
        iban.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(iban, 19, 1)

        iban_input = QLineEdit()
        iban_input.setInputMask("9999 9999 9999 9999;x")
        layout.addWidget(iban_input, 19, 2)

        pin = QLabel("PIN:")
        pin.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(pin, 20, 1)

        pin_input = QLineEdit()
        pin_input.setInputMask("999")
        pin_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(pin_input, 20, 2)

        cancel = QPushButton("Abbrechen")
        cancel.pressed.connect(self.rap_it_up)
        layout.addWidget(cancel, 21, 1)
        order = QPushButton("Bestellen")
        order.pressed.connect(self.rap_it_up)
        layout.addWidget(order, 21, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def add_text(self):
        text = self.text_browser.toPlainText()
        self.text_browser.setText(text + self.sender().text() + "\n")

    @pyqtSlot()
    def choose_pizza_size(self):

        self.add_text()

        if self.sender().text() == "Kleine Pizza":
            self.pizza_normal.setDisabled(True)
            self.pizza_family.setDisabled(True)

        if self.sender().text() == "Normale Pizza":
            self.pizza_small.setDisabled(True)
            self.pizza_family.setDisabled(True)

        if self.sender().text() == "Familien Pizza":
            self.pizza_normal.setDisabled(True)
            self.pizza_small.setDisabled(True)

        text = self.text_browser.toPlainText()
        self.text_browser.setText(text + "\n" + self.pizza_topings.text() + "\n")

    @pyqtSlot()
    def choose_drink(self):

        text = self.text_browser.toPlainText()
        self.text_browser.setText(text + "\n" + self.drinks.text() + "\n")

        self.add_text()

        if self.sender().text() == "Cola":
            self.fanta.setDisabled(True)
            self.sprite.setDisabled(True)
            self.water.setDisabled(True)

        if self.sender().text() == "Fanta":
            self.coke.setDisabled(True)
            self.sprite.setDisabled(True)
            self.water.setDisabled(True)

        if self.sender().text() == "Sprite":
            self.coke.setDisabled(True)
            self.fanta.setDisabled(True)
            self.water.setDisabled(True)

        if self.sender().text() == "Wasser":
            self.coke.setDisabled(True)
            self.fanta.setDisabled(True)
            self.sprite.setDisabled(True)

        text = self.text_browser.toPlainText()
        self.text_browser.setText(text + "\n" + self.where_to_eat.text() + "\n")

    @pyqtSlot()
    def choose_eating_place(self):

        self.add_text()

        if self.sender().text() == "Hier essen":
            self.to_go.setDisabled(True)

        if self.sender().text() == "To go":
            self.eat_hear.setDisabled(True)

    @pyqtSlot()
    def rap_it_up(self):

        if self.sender().text() == "Abbrechen":
            print("Die Bestellung wurde erfolgreich abgebrochen!")
            sys.exit()

        if self.sender().text() == "Bestellen":
            print("Die Besellung war erfolgreich!")
            sys.exit()
