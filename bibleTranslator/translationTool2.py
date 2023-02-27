import sys
import re
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import qtawesome


class Translator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("partial_Translate2.ui", self)

        # Load the book data from the JSON file
        with open('book_data.json', 'r') as f:
            self.book_data = json.load(f)

        # Extract the distinct book names, chapters, and verses from the book data
        # self.books = sorted(set([book['book'] for book in self.book_data]))
        # self.books = [book['book'] for book in self.book_data]
        self.books = [book_data['book'] for book_data in self.book_data if book_data['chapter'] == 1 and book_data['verse'] == 1]

        self.chapters = sorted(set([book['chapter'] for book in self.book_data]))
        self.verses = sorted(set([book['verse'] for book in self.book_data]))

        # Populate the book dropdown menu with the distinct book names
        self.bookDropdown.addItems(self.books)
        # self.bookDropdown.setCurrentText('Genesis')

        # Connect the button to a function
        self.TranslateWords_pushButton.clicked.connect(self.translate_text)
        self.previous_pushButton.clicked.connect(self.previous_verse)
        self.next_pushButton.clicked.connect(self.next_verse)

        # Populate the chapter and verse dropdowns with the numbers 1-50
        self.chapterDropdown.addItems([str(c) for c in range(1, 51)])
        self.verseDropdown.addItems([str(v) for v in range(1, 51)])

        # show the current verse
        self.show_verse()

    # show the current verse
    def show_verse(self):
        # Get the current book, chapter, and verse
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())

        # Get the text for the current verse
        verse_text = self.get_verse_text(book, chapter, verse)

        # Display the text in the textEdit field
        self.textEdit.setText(verse_text)

    # Get the text for the current verse
    def get_verse_text(self, book, chapter, verse):
        for book_data in self.book_data:
            if book_data['book'] == book and book_data['chapter'] == chapter and book_data['verse'] == verse:
                english_words = list(book_data['words'].keys())
                return ' '.join(english_words)
        return '' # return empty string if no matching verse is found
    
    def translate_text(self):
        # Get the text from the textEdit field
        text = self.textEdit.toPlainText()

        # Get the words to be translated and their translations from the JSON
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())
        verse_data = [book_data['words'] for book_data in self.book_data if book_data['book'] == book and book_data['chapter'] == chapter and book_data['verse'] == verse][0]

        # Get the words to be translated from the English_LineEdit field
        english_words = self.English_LineEdit.text()
        english_words_list = [word.strip() for word in english_words.split(",")]

        # If the English_LineEdit field is empty, change every word back to english (key)
        if english_words == '':
            self.show_verse()
        else:
            # Replace only the words listed in English_LineEdit
            for english in english_words_list:
                if english in verse_data:
                    hebrew = verse_data[english]
                    # Ignore case when replacing words
                    text = re.sub(r"\b" + english + r"\b", hebrew, text, flags=re.IGNORECASE)

        # Display the translated text
        self.textEdit.setText(text)




    def previous_verse(self):
        # Get the current book, chapter, and verse
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())

        # check the chapter if it is 1 and verse is 1 then return
        if chapter == 1 and verse == 1:
            return
        else:
            # Decrement the verse number
            verse -= 1

        # Get the text for the current verse
        verse_text = self.get_verse_text(book, chapter, verse)

        # Display the text in the textEdit field
        self.textEdit.setText(verse_text)

        # re-translate the text
        self.translate_text()

        # Set the dropdowns to the new book, chapter, and verse
        self.bookDropdown.setCurrentText(book)
        self.chapterDropdown.setCurrentText(str(chapter))
        self.verseDropdown.setCurrentText(str(verse))

        # Set the text in the textEdit field
        self.textEdit.setText(verse_text)


    def next_verse(self):
        # Get the current book, chapter, and verse
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())

        # Increment the verse number
        verse += 1

        # Get the text for the current verse
        verse_text = self.get_verse_text(book, chapter, verse)

        # Display the text in the textEdit field
        self.textEdit.setText(verse_text)
    
        # re-translate the text
        self.translate_text()

        # Set the dropdowns to the new book, chapter, and verse
        self.bookDropdown.setCurrentText(book)
        self.chapterDropdown.setCurrentText(str(chapter))
        self.verseDropdown.setCurrentText(str(verse))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = Translator()
    translator.show()
    sys.exit(app.exec())