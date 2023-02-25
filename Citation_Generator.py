import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QTextBrowser
import qtawesome
from PyQt6.QtGui import QClipboard

class CitationGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        note_label = QLabel('Text will be coppied to the clipboard')
        author_label = QLabel('Author Name:')
        date_label = QLabel('Date:')
        title_label = QLabel('Title:')
        publication_label = QLabel('Publication:')
        website_label = QLabel('Website:')
        output_label = QLabel('OUTPUT:')
        
        self.author_input = QLineEdit()
        self.date_input = QLineEdit()
        self.title_input = QLineEdit()
        self.publication_input = QLineEdit()
        self.website_input = QLineEdit()
        self.citation_output = QTextBrowser()
        
        generate_button = QPushButton('Generate Citation')
        generate_button.clicked.connect(self.generate_citation)

        # get font awesome
        # run `qta-browser` to look at all the available icons
        fa5_icon = qtawesome.icon('fa.copy')
        self.setWindowIcon(fa5_icon)

        layout = QFormLayout()
        layout.addRow(note_label)
        layout.addRow(author_label, self.author_input)
        layout.addRow(date_label, self.date_input)
        layout.addRow(title_label, self.title_input)
        layout.addRow(publication_label, self.publication_input)
        layout.addRow(website_label, self.website_input)
        layout.addRow(output_label, self.citation_output)
        layout.addRow(generate_button)
        
        self.setLayout(layout)
        self.setWindowTitle('Citation Generator')
        self.show()
        
    def generate_citation(self):
        author = self.author_input.text()
        date = self.date_input.text()
        title = self.title_input.text()
        publication = self.publication_input.text()
        website = self.website_input.text()
        
        author_initial = author.split()[0][0] + '.'
        author_last = author.split()[-1]
        
        citation = f'{author_last}, {author_initial} ({date}). {title}. {publication}. Retrieved from {website}.'
        self.citation_output.setText(citation)
        # copy to clipboard
        # copy the text to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(citation)

        # print(citation)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    citation_generator = CitationGenerator()
    sys.exit(app.exec())
