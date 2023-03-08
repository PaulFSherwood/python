import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout
from random import shuffle

class Flashcard(QWidget):
    def __init__(self, question, answer_options, correct_answer, parent=None):
        super().__init__(parent)

        self.question = question
        self.answer_options = answer_options
        self.correct_answer = correct_answer

        # Create a list of answer buttons
        self.answer_buttons = []
        for option in answer_options:
            button = QPushButton(f"a:{option}")
            button.setStyleSheet("QPushButton {background-color: white}")
            button.clicked.connect(lambda state, x=option: self.check_answer(x))
            self.answer_buttons.append(button)

        # Create a question label
        self.question_label = QLabel(self.question, self)
        self.question_label.setStyleSheet("font-size: 18pt")
        self.question_label.setWordWrap(True)

        # Create a flip button
        self.flip_button = QPushButton("Flip", self)
        self.flip_button.setStyleSheet("QPushButton {background-color: white}")
        self.flip_button.clicked.connect(self.flip_card)

        # Create a next button
        self.next_button = QPushButton("Next", self)
        self.next_button.setStyleSheet("QPushButton {background-color: white}")
        self.next_button.hide()
        self.next_button.clicked.connect(self.next_card)

        # Set up the layout
        self.answer_layout = QVBoxLayout()
        for button in self.answer_buttons:
            self.answer_layout.addWidget(button)
        self.answer_layout.addStretch()
        self.question_layout = QVBoxLayout()
        self.question_layout.addWidget(self.question_label)
        self.question_layout.addLayout(self.answer_layout)
        self.question_layout.addWidget(self.flip_button)
        self.question_layout.addWidget(self.next_button)
        self.setLayout(self.question_layout)

    def flip_card(self):
        # Show the answer when the flip button is pressed
        self.question_label.hide()
        for button in self.answer_buttons:
            button.hide()
        self.flip_button.hide()
        self.next_button.show()
        self.answer_label = QLabel(self.correct_answer, self)
        self.answer_label.setStyleSheet("font-size: 18pt; color: green")
        self.answer_layout.addWidget(self.answer_label)

    def check_answer(self, answer):
        # Check if the selected answer is correct
        for button in self.answer_buttons:
            if button.text() != f"a:{answer}":
                button.setStyleSheet("QPushButton {background-color: white}")
            else:
                if answer == self.correct_answer:
                    button.setStyleSheet("QPushButton {background-color: green}")
                else:
                    button.setStyleSheet("QPushButton {background-color: red}")
        if answer == self.correct_answer:
            for button in self.answer_buttons:
                button.setDisabled(True)

    def next_card(self):
        # Show the next flashcard when the next button is pressed
        self.parent().next_flashcard()

    def reset_card(self):
        # Reset the flashcard to the initial state
        self.answer_label.hide()
        self.question_label.show()
        for button in self.answer_buttons:
            button.show()
            button.setStyleSheet("QPushButton {background-color: white}")
            button.setEnabled(True)
        self.flip_button.show()
        self.next_button.hide()

class FlashcardWindow(QWidget):
    def __init__(self, flashcards):
        super().__init__()

        self.flashcards = flashcards
        self.current_card_index = 0

        # Create the flashcard widgets
        self.flashcard_widgets = []
        for flashcard in self.flashcards:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(flashcard)
            self.flashcard_widgets.append(widget)

        # Set up the layout
        self.stack_layout = QStackedLayout()
        for widget in self.flashcard_widgets:
            self.stack_layout.addWidget(widget)
        self.setLayout(self.stack_layout)

    def reset_card(self):
        # Reset the flashcard to the initial state
        self.flashcards[self.current_card_index].reset_card()

    def next_flashcard(self):
        # Show the next flashcard in the list
        self.current_card_index += 1
        if self.current_card_index < len(self.flashcards):
            self.stack_layout.setCurrentIndex(self.current_card_index)
            self.reset_card()
        else:
            self.close()

def create_flashcards():
    # Define the list of questions and answers
    question_options = [
        ("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
        ("What is the largest planet in our solar system?", ["Jupiter", "Mars", "Earth"], "Jupiter"),
        ("What is the smallest country in the world?", ["Vatican City", "Monaco", "Liechtenstein"], "Vatican City"),
        ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], "Leonardo da Vinci"),
        ("What is the tallest mammal?", ["Giraffe", "Elephant", "Hippopotamus"], "Giraffe"),
        ("What is the largest animal in the world?", ["Blue whale", "Elephant", "Giraffe"], "Blue whale"),
        ("What is the capital of Spain?", ["Madrid", "Barcelona", "Seville"], "Madrid"),
        ("What is the capital of Japan?", ["Tokyo", "Kyoto", "Osaka"], "Tokyo"),
        ("What is the capital of Italy?", ["Rome", "Milan", "Florence"], "Rome"),
        ("What is the currency of Russia?", ["Ruble", "Dollar", "Euro"], "Ruble"),
    ]

    # Shuffle the questions and create the flashcards
    shuffle(question_options)
    flashcards = []
    for question, options, answer in question_options:
        flashcards.append(Flashcard(question, options, answer))

    return flashcards

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the flashcards
    flashcards = create_flashcards()

    # Create the window and show the first flashcard
    window = FlashcardWindow(flashcards)
    window.show()
    window.setMinimumSize(500, 400)

    # Run the main loop
    sys.exit(app.exec_())
