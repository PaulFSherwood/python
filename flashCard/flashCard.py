                f"Correct answer: {self.shuffled_correct}\n\nReason:\n{card.reason}",
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

