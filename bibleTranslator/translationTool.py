import sys, re
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import qtawesome

# Translation class
# English_LineEdit: input english words separated by comma and a space
# Translate_LineEdit: input alt language words seperated by comma and a space
# textEdit: Output field to show the translate text
# TranslateWords_pushButton: Button to call the translate_text function
class Translator(QtWidgets.QMainWindow):  
    def __init__(self):
            super().__init__()
            loadUi("partial_Translate.ui", self)

            # Create an icon `qta-browser`
            self.icon = qtawesome.icon("mdi.google-translate", color="#404258")
            self.setWindowIcon(self.icon)

            # Connect the button to a function
            self.TranslateWords_pushButton.clicked.connect(self.translate_text)

            # Set default values for the words to be translated and their translation
            self.English_LineEdit.setText("the, to, of, and")
            self.Translate_LineEdit.setText("η, εἰς, από, και")
            self.textEdit.setText("The I'm going to the park to play with my friends and enjoy the sunshine of the day.")
            # self.English_LineEdit.setText("to, the, of, and")
            # self.Translate_LineEdit.setText("προς, η, από, και")

    # this function replaces English_LineEdit words with Translate_LineEdit words
    def translate_text(self):
        # Get the text from the textEdit field
        text = self.textEdit.toPlainText()
        # Get the words to be translated and their translation
        EnglishWords = self.English_LineEdit.text()
        TranslateWords = self.Translate_LineEdit.text()
        # Split the words into a list
        EnglishWords = EnglishWords.split(", ")
        TranslateWords = TranslateWords.split(", ")
        # Replace the words in the text
        for i in range(len(EnglishWords)):
            # Ingore case when replacing words
            text = re.sub(r"\b" + EnglishWords[i] + r"\b", TranslateWords[i], text, flags=re.IGNORECASE)
        # Display the translated text
        self.textEdit.setText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = Translator()
    translator.show()
    sys.exit(app.exec())
