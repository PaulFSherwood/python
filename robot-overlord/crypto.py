import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox

class CryptoInvest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CryptoInvest')
        self.setGeometry(100, 100, 300, 250)

        self.amount_label = QLabel('Amount to Invest (USD):')
        self.amount_input = QLineEdit()
        self.crypto_label = QLabel('Select Cryptocurrency:')
        self.crypto_select = QComboBox()
        self.crypto_select.addItems(['Bitcoin', 'Ethereum', 'Litecoin', 'Dogecoin'])
        self.buy_button = QPushButton('Buy')
        self.buy_button.clicked.connect(self.buy_crypto)

        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.crypto_label)
        layout.addWidget(self.crypto_select)
        layout.addWidget(self.buy_button)

        self.setLayout(layout)

    def buy_crypto(self):
        amount = self.amount_input.text()
        crypto = self.crypto_select.currentText()

        # API URL for Coinbase
        url = 'https://api.coinbase.com/v2/prices/{crypto}-USD/buy'

        # Set headers
        headers = {'Authorization': 'Bearer <YOUR_API_KEY>'}

        # Set payload
        payload = {'amount': amount}

        # Send POST request to Coinbase API
        response = requests.post(url.format(crypto=crypto), headers=headers, data=payload)

        # Check response status
        if response.status_code == 201:
            message = f'You have successfully bought {amount} USD of {crypto}!'
        else:
            message = 'There was an error with your order.'

        # Show message box with result
        QMessageBox.information(self, 'Order Result', message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CryptoInvest()
    window.show()
    sys.exit(app.exec_())
