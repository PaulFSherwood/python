import sys
from typing import List
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QStackedLayout
from random import shuffle, sample

class Flashcard(QWidget):
    def __init__(self, question: str, answer_options: List[str], correct_answer: str, parent=None):
        super().__init__(parent)
        self.parent_window = parent

        self.question = question
        self.answer_options = answer_options
        self.correct_answer = correct_answer

        # Create a list of answer buttons
        self.answer_buttons = []
        for option in answer_options:
            button = QPushButton(f"a:{option}")
            button.setStyleSheet("QPushButton {background-color: grey}")
            button.clicked.connect(lambda state, x=option: self.check_answer(x))
            self.answer_buttons.append(button)

        # Create a question label
        self.question_label = QLabel(self.question, self)
        self.question_label.setStyleSheet("font-size: 18pt")
        self.question_label.setWordWrap(True)


        # Create a next button
        self.next_button = QPushButton("Next", self)
        self.next_button.setStyleSheet("QPushButton {background-color: grey}")
        self.next_button.clicked.connect(self.next_card)

        # Set up the layout
        self.answer_layout = QVBoxLayout()
        for button in self.answer_buttons:
            self.answer_layout.addWidget(button)
        self.answer_layout.addStretch()
        self.question_layout = QVBoxLayout()
        self.question_layout.addWidget(self.question_label)
        self.question_layout.addLayout(self.answer_layout)
        self.question_layout.addWidget(self.next_button)
        self.setLayout(self.question_layout)



    def check_answer(self, answer):
        # Check if the selected answer is correct
        for button in self.answer_buttons:
            if button.text() != f"a:{answer}":
                button.setStyleSheet("QPushButton {background-color: grey}")
            else:
                if answer == self.correct_answer:
                    button.setStyleSheet("QPushButton {background-color: green}")
                else:
                    button.setStyleSheet("QPushButton {background-color: red}")
        if answer == self.correct_answer:
            for button in self.answer_buttons:
                button.setDisabled(True)

    def next_card(self):
        if self.parent_window:
            self.parent_window.next_flashcard()

        # FlashcardWindow.next_flashcard()

    def reset_card(self):
        # Reset the flashcard to the initial state
        # self.answer_label.hide()
        self.question_label.show()
        for button in self.answer_buttons:
            button.show()
            button.setStyleSheet("QPushButton {background-color: grey}")
            button.setEnabled(True)




class FlashcardWindow(QWidget):
    def __init__(self, flashcards):
        super().__init__()
        self.flashcards = flashcards
        self.current_card_index = 0
        self.setup_flashcards()

    def setup_flashcards(self):
        # Create the flashcard widgets and their containers
        self.flashcard_containers = []
        for flashcard in self.flashcards:
            container = QWidget()
            layout = QVBoxLayout(container)
            layout.addWidget(flashcard)
            self.flashcard_containers.append(container)

        # Set up the layout
        self.stack_layout = QStackedLayout()
        for container in self.flashcard_containers:
            self.stack_layout.addWidget(container)
        self.setLayout(self.stack_layout)

    def reset_card(self):
        self.flashcards[self.current_card_index].reset_card()

    def next_flashcard(self):
        self.current_card_index += 1
        if self.current_card_index < len(self.flashcards):
            self.stack_layout.setCurrentIndex(self.current_card_index)
            self.reset_card()
        else:
            self.close()

def load_flashcards_from_file(file_name, parent_window):
    with open(file_name, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    flashcards = []
    for question, answer in lines:
        # Exclude the current question's answer from the options
        other_answers = [a for q, a in lines if q != question]
        all_answers = [answer] + sample(other_answers, min(3, len(other_answers)))
        shuffle(all_answers)
        flashcards.append(Flashcard(question, all_answers, answer, parent=parent_window))

    return flashcards

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # flashcards = load_flashcards_from_file('flashcard_data.txt')
    flashcards = load_flashcards_from_file('flashcard_data.txt', None)

    window = FlashcardWindow(flashcards)

    for flashcard in flashcards:
        flashcard.parent_window = window

    window.show()
    window.setMinimumSize(500, 400)

    sys.exit(app.exec_())
