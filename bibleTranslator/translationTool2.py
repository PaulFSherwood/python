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
        self.books = sorted(set([book['book'] for book in self.book_data]))
        self.chapters = sorted(set([book['chapter'] for book in self.book_data]))
        self.verses = sorted(set([book['verse'] for book in self.book_data]))

        # Populate the book dropdown menu with the distinct book names
        self.bookDropdown.addItems(self.books)

        # Connect the button to a function
        self.TranslateWords_pushButton.clicked.connect(self.translate_text)
        self.previous_pushButton.clicked.connect(self.previous_verse)
        self.next_pushButton.clicked.connect(self.next_verse)

        # Populate the chapter and verse dropdowns with the numbers 1-50
        self.chapterDropdown.addItems([str(c) for c in range(1, 51)])
        self.verseDropdown.addItems([str(v) for v in range(1, 51)])

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

    def previous_verse(self):
        # Get the current book, chapter, and verse
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())

        # Decrement the verse number
        verse -= 1

        # If the verse is less than 1, decrement the chapter and set the verse to the last verse in the chapter
        if verse < 1:
            chapter -= 1
            if chapter < 1:
                # If the chapter is less than 1, go to the last chapter in the previous book
                book_index = self.books.index(book)
                if book_index > 0:
                    book = self.books[book_index - 1]
                    chapter = self.chapters[-1]
                    verse = self.verses[-1]
                else:
                    # If the current book is Genesis, the previous button does nothing
                    return
            else:
                # Set the verse to the last verse in the previous chapter
                verse = max([book['verse'] for book in self.book_data if book['book'] == book and book['chapter'] == chapter])

        # Set the dropdowns to the new book, chapter, and verse
        self.bookDropdown.setCurrentText(book)
        self.chapterDropdown.setCurrentText(str(chapter))
        self.verseDropdown.setCurrentText(str(verse))

        # Get the text for the new verse from the book data
        for book_data in self.book_data:
            if book_data['book'] == book and book_data['chapter'] == chapter and book_data['verse'] == verse:
                verse_text = book_data['words']
                break
        else:
            verse_text = ''

        # Set the text in the textEdit field
        self.textEdit.setText(verse_text)


    def next_verse(self):
        # Get the current book, chapter, and verse
        book = self.bookDropdown.currentText()
        chapter = int(self.chapterDropdown.currentText())
        verse = int(self.verseDropdown.currentText())

        # Increment the verse number
        verse += 1

        # If the verse is greater than the last verse in the chapter, increment the chapter and set the verse to 1
        max_verse = max([book['verse'] for book in self.book_data if book['book'] == book and book['chapter'] == chapter])
        if verse > max_verse:
            chapter += 1
            if chapter > self.chapters[-1]:
                # If the chapter is greater than the last chapter in the current book, go to the first chapter in the next book
                book_index = self.books.index(book)
                if book_index < len(self.books) - 1:
                    book = self.books[book_index + 1]
                    chapter = 1
                    verse = 1
                else:
                    # If the current book is Malachi, the next button does nothing
                    return
            else:
                # Set the verse to 1 in the next chapter
                verse = 1

        # Set the dropdowns to the new book, chapter, and verse
        self.bookDropdown.setCurrentText(book)
        self.chapterDropdown.setCurrentText(str(chapter))
        self.verseDropdown.setCurrentText(str(verse))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = Translator()
    translator.show()
    sys.exit(app.exec())