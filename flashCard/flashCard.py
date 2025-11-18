import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QLineEdit, QComboBox,
    QMessageBox
)
from PyQt6.QtCore import Qt


FLASHCARD_FILE = "flashcards.json"


class FlashCard:
    def __init__(self, question, answers, correct_index, reason):
        self.question = question
        self.answers = answers
        self.correct_index = correct_index
        self.reason = reason

    def to_dict(self):
        return {
            "question": self.question,
            "answers": self.answers,
            "correct_index": self.correct_index,
            "reason": self.reason
        }

    @staticmethod
    def from_dict(data):
        return FlashCard(
            data["question"],
            data["answers"],
            data["correct_index"],
            data["reason"]
        )


class FlashCardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Flash Cards")

        self.flashcards = []
        self.current_index = 0
        self.correct = 0
        self.wrong = 0

        self.load_cards()
        self.init_ui()

        if self.flashcards:
            self.display_card(0)

    # -------------------------------------------
    # LOAD / SAVE
    # -------------------------------------------
    def load_cards(self):
        if os.path.exists(FLASHCARD_FILE):
            try:
                with open(FLASHCARD_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.flashcards = [FlashCard.from_dict(item) for item in data]
            except Exception as e:
                print("Error loading flashcards:", e)

    def save_cards(self):
        try:
            with open(FLASHCARD_FILE, "w", encoding="utf-8") as f:
                json.dump([c.to_dict() for c in self.flashcards], f, indent=4)
        except Exception as e:
            print("Error saving flashcards:", e)

    # -------------------------------------------
    # UI
    # -------------------------------------------
    def init_ui(self):
        layout = QVBoxLayout()

        # --- Add Card Section ---
        self.question_edit = QTextEdit()
        self.question_edit.setPlaceholderText("Enter question here (supports ```cpp code blocks```)")
        layout.addWidget(QLabel("Question:"))
        layout.addWidget(self.question_edit)

        self.answer_edits = []
        for i in range(4):
            le = QLineEdit()
            le.setPlaceholderText(f"Answer option {i+1}")
            self.answer_edits.append(le)
            layout.addWidget(le)

        layout.addWidget(QLabel("Correct answer index (0-3):"))
        self.correct_box = QComboBox()
        self.correct_box.addItems(["0", "1", "2", "3"])
        layout.addWidget(self.correct_box)

        self.reason_edit = QTextEdit()
        self.reason_edit.setPlaceholderText("Explanation / Reason for the answer")
        layout.addWidget(QLabel("Reason:"))
        layout.addWidget(self.reason_edit)

        add_btn = QPushButton("➕ Add Flash Card")
        add_btn.clicked.connect(self.add_flashcard)
        layout.addWidget(add_btn)

        # --- Review Section ---
        self.review_area = QTextEdit()
        self.review_area.setReadOnly(True)
        layout.addWidget(QLabel("Flash Card Review:"))
        layout.addWidget(self.review_area)

        # Answer buttons
        self.answer_buttons = []
        btn_row = QHBoxLayout()
        for i in range(4):
            btn = QPushButton(f"Answer {i+1}")
            btn.clicked.connect(lambda _, idx=i: self.check_answer(idx))
            self.answer_buttons.append(btn)
            btn_row.addWidget(btn)
        layout.addLayout(btn_row)

        # Navigation
        nav_row = QHBoxLayout()
        prev_btn = QPushButton("⬅ Previous")
        next_btn = QPushButton("Next ➡")
        prev_btn.clicked.connect(self.prev_card)
        next_btn.clicked.connect(self.next_card)
        nav_row.addWidget(prev_btn)
        nav_row.addWidget(next_btn)
        layout.addLayout(nav_row)

        self.score_label = QLabel("Score: 0 correct / 0 wrong")
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    # -------------------------------------------
    # ADD FLASH CARD
    # -------------------------------------------
    def add_flashcard(self):
        question = self.question_edit.toPlainText().strip()
        answers = [a.text().strip() for a in self.answer_edits]
        reason = self.reason_edit.toPlainText().strip()
        correct = int(self.correct_box.currentText())

        if not question or any(a == "" for a in answers):
            QMessageBox.warning(self, "Error", "Please fill out all fields.")
            return

        card = FlashCard(question, answers, correct, reason)
        self.flashcards.append(card)
        self.save_cards()

        QMessageBox.information(self, "Added", "Flash card saved!")

        self.question_edit.clear()
        for a in self.answer_edits:
            a.clear()
        self.reason_edit.clear()

        self.display_card(len(self.flashcards) - 1)

    # -------------------------------------------
    # REVIEW / DISPLAY
    # -------------------------------------------
    def display_card(self, index):
        if not self.flashcards:
            self.review_area.setHtml("No cards yet.")
            return

        card = self.flashcards[index]
        text = f"<b>Question:</b><br>{self.format_with_code(card.question)}<br><br>"

        for i, ans in enumerate(card.answers):
            text += f"{i}. {ans}<br>"

        self.review_area.setHtml(text)

    # -------------------------------------------
    # CHECK ANSWER
    # -------------------------------------------
    def check_answer(self, idx):
        if not self.flashcards:
            return

        card = self.flashcards[self.current_index]
        if idx == card.correct_index:
            self.correct += 1
            QMessageBox.information(self, "Correct!", "Nice!")
        else:
            self.wrong += 1
            QMessageBox.warning(
                self,
                "Incorrect",
                f"Correct answer: {card.correct_index}\n\nReason:\n{card.reason}",
            )

        self.score_label.setText(f"Score: {self.correct} correct / {self.wrong} wrong")

    # -------------------------------------------
    # NAVIGATION
    # -------------------------------------------
    def next_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.display_card(self.current_index)

    def prev_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.display_card(self.current_index)

    # -------------------------------------------
    # CODE BLOCK RENDERING
    # -------------------------------------------
    def format_with_code(self, text):
        import re
        blocks = re.split(r"```cpp|```", text)

        if len(blocks) == 1:
            return text.replace("\n", "<br>")

        result = ""
        is_code = False

        for part in blocks:
            if is_code:
                result += f"<pre style='background:#1e1e1e;color:#9cdcfe;padding:6px;'>{part}</pre>"
            else:
                result += part.replace("\n", "<br>")
            is_code = not is_code

        return result


# -------------------------------------------
# MAIN
# -------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlashCardApp()
    window.resize(800, 900)
    window.show()
    sys.exit(app.exec())

