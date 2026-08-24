#!/usr/bin/env python3
"""
CSEP Study v2
A polished PyQt6 flashcard / practice-exam GUI for csep_questions_v2.json.

Install:
    python3 -m pip install PyQt6

Run:
    python3 csep_study_v2.py
"""

from __future__ import annotations

import json
import random
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    from PyQt6.QtCore import Qt, QTimer
    from PyQt6.QtGui import QKeySequence, QShortcut
    from PyQt6.QtWidgets import (
        QApplication, QCheckBox, QComboBox, QFileDialog, QFrame, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMessageBox, QProgressBar, QPushButton,
        QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
    )
except ImportError as exc:
    raise SystemExit(
        "PyQt6 is required.\nInstall it with:\n python3 -m pip install PyQt6"
    ) from exc

APP_TITLE = "CSEP Study"
DEFAULT_BANK = Path(__file__).with_name("csep_questions_v2.json")
PROGRESS_FILE = Path.home() / ".csep_study_v2_progress.json"


@dataclass
class Question:
    topic: str
    difficulty: str
    question: str
    answers: list[str]
    correct_index: int
    reason: str


def normalize(text: str) -> str:
    text = re.sub(r"[^a-z0-9 ]+", "", text.lower())
    return re.sub(r"\s+", " ", text).strip()


class AnswerButton(QPushButton):
    def __init__(self, index: int):
        super().__init__()
        self.index = index
        self.setCheckable(False)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(72)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.setProperty("answerState", "normal")

    def set_state(self, state: str):
        self.setProperty("answerState", state)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()


class StudyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.resize(1120, 820)
        self.setMinimumSize(900, 680)

        self.bank_path = DEFAULT_BANK
        self.all_questions: list[Question] = []
        self.session_questions: list[Question] = []
        self.current = 0
        self.session_correct = 0
        self.session_wrong = 0
        self.answered = False
        self.current_display_answers: list[tuple[str, bool]] = []
        self.progress = self.load_progress()
        self.last_validation_warnings: list[str] = []

        self.build_ui()
        self.apply_style()
        self.install_shortcuts()

        if self.bank_path.exists():
            self.load_bank(self.bank_path)
        else:
            self.choose_bank()

    # ---------- UI ----------
    def build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)
        outer = QHBoxLayout(root)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(250)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(22, 26, 22, 22)
        side.setSpacing(14)

        brand = QLabel("CSEP")
        brand.setObjectName("brand")
        subtitle = QLabel("SYSTEMS ENGINEERING\nPRACTICE")
        subtitle.setObjectName("brandSubtitle")
        side.addWidget(brand)
        side.addWidget(subtitle)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setObjectName("divider")
        side.addWidget(divider)

        label = QLabel("TOPIC")
        label.setObjectName("sectionLabel")
        self.topic_combo = QComboBox()
        self.topic_combo.currentTextChanged.connect(self.rebuild_session)
        side.addWidget(label)
        side.addWidget(self.topic_combo)

        self.missed_only = QCheckBox("Missed questions only")
        self.missed_only.toggled.connect(self.rebuild_session)
        side.addWidget(self.missed_only)

        self.shuffle_questions = QCheckBox("Shuffle question order")
        self.shuffle_questions.setChecked(True)
        side.addWidget(self.shuffle_questions)

        self.new_session_btn = QPushButton("New Session")
        self.new_session_btn.setObjectName("primaryButton")
        self.new_session_btn.clicked.connect(self.new_session)
        side.addWidget(self.new_session_btn)

        self.load_btn = QPushButton("Load Question Bank")
        self.load_btn.clicked.connect(self.choose_bank)
        side.addWidget(self.load_btn)

        side.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.bank_label = QLabel("No bank loaded")
        self.bank_label.setWordWrap(True)
        self.bank_label.setObjectName("muted")
        side.addWidget(self.bank_label)

        self.audit_label = QLabel("")
        self.audit_label.setWordWrap(True)
        self.audit_label.setObjectName("auditGood")
        side.addWidget(self.audit_label)

        outer.addWidget(sidebar)

        # Main content
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(34, 26, 34, 28)
        content_layout.setSpacing(16)

        top = QHBoxLayout()
        title_box = QVBoxLayout()
        self.mode_label = QLabel("PRACTICE SESSION")
        self.mode_label.setObjectName("eyebrow")
        self.title_label = QLabel("Systems Engineering Knowledge")
        self.title_label.setObjectName("pageTitle")
        title_box.addWidget(self.mode_label)
        title_box.addWidget(self.title_label)
        top.addLayout(title_box)
        top.addStretch()

        self.score_chip = QLabel("0 correct - 0 wrong")
        self.score_chip.setObjectName("scoreChip")
        top.addWidget(self.score_chip)
        content_layout.addLayout(top)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(8)
        content_layout.addWidget(self.progress_bar)

        self.status_line = QLabel("Question 0 of 0")
        self.status_line.setObjectName("muted")
        content_layout.addWidget(self.status_line)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        viewport = QWidget()
        v = QVBoxLayout(viewport)
        v.setContentsMargins(0, 0, 0, 0)
        v.setSpacing(16)

        question_card = QFrame()
        question_card.setObjectName("questionCard")
        qlayout = QVBoxLayout(question_card)
        qlayout.setContentsMargins(26, 24, 26, 24)
        qlayout.setSpacing(12)

        badges = QHBoxLayout()
        self.topic_badge = QLabel("Topic")
        self.topic_badge.setObjectName("topicBadge")
        self.diff_badge = QLabel("Difficulty")
        self.diff_badge.setObjectName("diffBadge")
        badges.addWidget(self.topic_badge)
        badges.addWidget(self.diff_badge)
        badges.addStretch()
        qlayout.addLayout(badges)

        self.question_label = QLabel("Load a question bank to begin.")
        self.question_label.setWordWrap(True)
        self.question_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.question_label.setObjectName("questionText")
        qlayout.addWidget(self.question_label)

        v.addWidget(question_card)

        self.answer_buttons: list[AnswerButton] = []
        for i in range(4):
            btn = AnswerButton(i)
            btn.clicked.connect(lambda checked=False, n=i: self.answer(n))
            self.answer_buttons.append(btn)
            v.addWidget(btn)

        self.explanation = QFrame()
        self.explanation.setObjectName("explanationCard")
        exp = QVBoxLayout(self.explanation)
        exp.setContentsMargins(22, 18, 22, 18)
        self.result_label = QLabel("")
        self.result_label.setObjectName("resultLabel")
        self.reason_label = QLabel("")
        self.reason_label.setWordWrap(True)
        self.reason_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.reason_label.setObjectName("reasonText")
        exp.addWidget(self.result_label)
        exp.addWidget(self.reason_label)
        self.explanation.hide()
        v.addWidget(self.explanation)

        v.addStretch()
        scroll.setWidget(viewport)
        content_layout.addWidget(scroll, 1)

        nav = QHBoxLayout()
        self.prev_btn = QPushButton("<- Previous")
        self.prev_btn.clicked.connect(self.previous_question)
        self.next_btn = QPushButton("Next ->")
        self.next_btn.setObjectName("primaryButton")
        self.next_btn.clicked.connect(self.next_question)
        nav.addWidget(self.prev_btn)
        nav.addStretch()
        shortcut_hint = QLabel("1-4 answer - <-/->’ navigate - N new session")
        shortcut_hint.setObjectName("muted")
        nav.addWidget(shortcut_hint)
        nav.addStretch()
        nav.addWidget(self.next_btn)
        content_layout.addLayout(nav)

        outer.addWidget(content, 1)

    def apply_style(self):
        self.setStyleSheet("""
        QWidget {
        background: #0c111b;
        color: #eef3fb;
        font-family: "Inter", "Segoe UI", "Noto Sans", sans-serif;
        font-size: 14px;
        }
        #sidebar {
        background: #111827;
        border-right: 1px solid #263247;
        }
        #brand {
        color: #ffffff;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 2px;
        }
        #brandSubtitle, #eyebrow, #sectionLabel {
        color: #7aa2f7;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        }
        #pageTitle {
        color: #ffffff;
        font-size: 25px;
        font-weight: 750;
        }
        #muted {
        color: #8f9caf;
        font-size: 12px;
        }
        #divider {
        color: #263247;
        background: #263247;
        max-height: 1px;
        margin: 8px 0;
        }
        QComboBox {
        background: #182235;
        border: 1px solid #2d3c56;
        border-radius: 8px;
        padding: 9px 10px;
        color: #f5f7fb;
        }
        QComboBox:hover { border-color: #5272a7; }
        QCheckBox { color: #cad4e3; spacing: 8px; }
        QCheckBox::indicator {
        width: 17px; height: 17px;
        border: 1px solid #465674;
        border-radius: 4px;
        background: #111827;
        }
        QCheckBox::indicator:checked {
        background: #3b82f6;
        border-color: #60a5fa;
        }
        QPushButton {
        background: #182235;
        border: 1px solid #2d3c56;
        border-radius: 9px;
        padding: 10px 15px;
        color: #e7edf7;
        font-weight: 600;
        }
        QPushButton:hover {
        background: #202d44;
        border-color: #4c648c;
        }
        QPushButton:disabled {
        color: #69768a;
        background: #121a28;
        border-color: #263247;
        }
        #primaryButton {
        background: #2563eb;
        border-color: #3b82f6;
        color: white;
        }
        #primaryButton:hover { background: #2f6ef2; }
        #scoreChip {
        background: #151f30;
        border: 1px solid #2b3a53;
        border-radius: 14px;
        padding: 7px 12px;
        color: #cbd7e8;
        font-weight: 650;
        }
        QProgressBar {
        background: #172033;
        border: none;
        border-radius: 4px;
        }
        QProgressBar::chunk {
        background: #3b82f6;
        border-radius: 4px;
        }
        #questionCard, #explanationCard {
        background: #121a28;
        border: 1px solid #263247;
        border-radius: 14px;
        }
        #questionText {
        background: transparent;
        font-size: 20px;
        font-weight: 650;
        line-height: 1.45;
        padding-top: 6px;
        }
        #topicBadge {
        background: #172554;
        color: #93c5fd;
        border: 1px solid #24458c;
        border-radius: 9px;
        padding: 4px 9px;
        font-size: 11px;
        font-weight: 700;
        }
        #diffBadge {
        background: #262033;
        color: #d8b4fe;
        border: 1px solid #49355d;
        border-radius: 9px;
        padding: 4px 9px;
        font-size: 11px;
        font-weight: 700;
        }
        AnswerButton, QPushButton[answerState="normal"] {
        text-align: left;
        background: #121a28;
        border: 1px solid #2b3950;
        border-radius: 12px;
        padding: 15px 18px;
        color: #eef3fb;
        font-size: 15px;
        font-weight: 550;
        }
        QPushButton[answerState="normal"]:hover {
        background: #182438;
        border-color: #5471a3;
        }
        QPushButton[answerState="correct"] {
        text-align: left;
        background: #103023;
        border: 1px solid #2f9b6d;
        border-radius: 12px;
        padding: 15px 18px;
        color: #d9ffec;
        font-size: 15px;
        font-weight: 650;
        }
        QPushButton[answerState="wrong"] {
        text-align: left;
        background: #35181d;
        border: 1px solid #b34d5c;
        border-radius: 12px;
        padding: 15px 18px;
        color: #ffe3e8;
        font-size: 15px;
        font-weight: 650;
        }
        QPushButton[answerState="dim"] {
        text-align: left;
        background: #101722;
        border: 1px solid #202b3e;
        border-radius: 12px;
        padding: 15px 18px;
        color: #77859a;
        font-size: 15px;
        }
        #explanationCard {
        background: #101a2a;
        border-color: #294164;
        }
        #resultLabel {
        background: transparent;
        color: #ffffff;
        font-size: 16px;
        font-weight: 750;
        }
        #reasonText {
        background: transparent;
        color: #c5d0df;
        font-size: 14px;
        padding-top: 6px;
        }
        #auditGood {
        color: #86efac;
        font-size: 11px;
        }
        #auditWarn {
        color: #fbbf24;
        font-size: 11px;
        }
        QScrollArea { background: transparent; }
        QScrollBar:vertical {
        background: #0d1420;
        width: 10px;
        margin: 0;
        }
        QScrollBar::handle:vertical {
        background: #35445c;
        min-height: 30px;
        border-radius: 5px;
        }
        """)

    def install_shortcuts(self):
        for i, key in enumerate(("1", "2", "3", "4")):
            sc = QShortcut(QKeySequence(key), self)
            sc.activated.connect(lambda n=i: self.answer(n))
        QShortcut(QKeySequence(Qt.Key.Key_Right), self).activated.connect(self.next_question)
        QShortcut(QKeySequence(Qt.Key.Key_Left), self).activated.connect(self.previous_question)
        QShortcut(QKeySequence("N"), self).activated.connect(self.new_session)

    # ---------- Bank loading / validation ----------
    def choose_bank(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open CSEP Question Bank",
            str(self.bank_path.parent if self.bank_path else Path.home()),
            "JSON files (*.json);;All files (*)"
        )
        if path:
            self.load_bank(Path(path))

    def load_bank(self, path: Path):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            rows = raw.get("questions", raw) if isinstance(raw, dict) else raw
            if not isinstance(rows, list):
                raise ValueError("Question bank must be a list or contain a 'questions' list.")

            questions = []
            for n, item in enumerate(rows, start=1):
                answers = item["answers"]
                q = Question(
                    topic=str(item.get("topic", "General")),
                    difficulty=str(item.get("difficulty", "Practice")),
                    question=str(item["question"]).strip(),
                    answers=[str(a).strip() for a in answers],
                    correct_index=int(item["correct_index"]),
                    reason=str(item.get("reason", "")).strip(),
                )
                if len(q.answers) != 4:
                    raise ValueError(f"Question {n} does not have exactly four answers.")
                if not (0 <= q.correct_index < 4):
                    raise ValueError(f"Question {n} has invalid correct_index.")
                questions.append(q)

            warnings = self.audit_bank(questions)
            self.all_questions = questions
            self.bank_path = path
            self.last_validation_warnings = warnings
            self.bank_label.setText(f"{path.name}\n{len(questions)} questions")

            if warnings:
                self.audit_label.setObjectName("auditWarn")
                self.audit_label.setText("Bank audit: " + " • ".join(warnings[:3]))
            else:
                self.audit_label.setObjectName("auditGood")
                self.audit_label.setText("Bank audit passed")
            self.audit_label.style().unpolish(self.audit_label)
            self.audit_label.style().polish(self.audit_label)

            self.populate_topics()
            self.new_session()

            if warnings:
                QMessageBox.warning(
                self, "Question bank warning",
                "The bank loaded, but quality checks found:\n\n• " + "\n• ".join(warnings)
                )

        except Exception as exc:
            QMessageBox.critical(self, "Could not load question bank", str(exc))

    def audit_bank(self, questions: list[Question]) -> list[str]:
        warnings = []
        if not questions:
            return ["No questions found"]

        qkeys = [normalize(q.question) for q in questions]
        dup_q = len(qkeys) - len(set(qkeys))
        if dup_q:
            warnings.append(f"{dup_q} duplicate question(s)")

        bad_answers = sum(1 for q in questions if len({normalize(a) for a in q.answers}) != 4)
        if bad_answers:
            warnings.append(f"{bad_answers} question(s) contain duplicate answers")

        answer_sets = [tuple(sorted(normalize(a) for a in q.answers)) for q in questions]
        repeated_sets = len(answer_sets) - len(set(answer_sets))
        if repeated_sets:
            warnings.append(f"{repeated_sets} repeated four-answer set(s)")

        counts = [sum(1 for q in questions if q.correct_index == i) for i in range(4)]
        if max(counts) / len(questions) > 0.65:
            warnings.append("correct-answer positions are suspiciously concentrated")

        generic_reason = sum(
            1 for q in questions
            if "best aligns with standard systems engineering practices" in q.reason.lower()
        )
        if generic_reason > max(3, len(questions) * 0.1):
            warnings.append("too many generic explanations")

        return warnings

    def populate_topics(self):
        current = self.topic_combo.currentText()
        self.topic_combo.blockSignals(True)
        self.topic_combo.clear()
        self.topic_combo.addItem("All topics")
        for topic in sorted({q.topic for q in self.all_questions}):
            self.topic_combo.addItem(topic)
        idx = self.topic_combo.findText(current)
        self.topic_combo.setCurrentIndex(idx if idx >= 0 else 0)
        self.topic_combo.blockSignals(False)

    # ---------- Session ----------
    def new_session(self):
        self.session_correct = 0
        self.session_wrong = 0
        self.rebuild_session(reset_stats=False)

    def rebuild_session(self, *_args, reset_stats=False):
        if not self.all_questions:
            return

        topic = self.topic_combo.currentText() or "All topics"
        pool = [
            q for q in self.all_questions
            if topic == "All topics" or q.topic == topic
        ]

        if self.missed_only.isChecked():
            missed = set(self.progress.get("missed", []))
            pool = [q for q in pool if self.question_id(q) in missed]

        self.session_questions = pool[:]
        if self.shuffle_questions.isChecked():
            random.shuffle(self.session_questions)

        self.current = 0
        self.answered = False
        self.refresh_score()

        if not self.session_questions:
            self.question_label.setText("No questions match the current filter.")
            for b in self.answer_buttons:
                b.hide()
            self.explanation.hide()
            self.status_line.setText("0 questions")
            self.progress_bar.setValue(0)
            return

        for b in self.answer_buttons:
            b.show()
        self.show_question()

    def question_id(self, q: Question) -> str:
        base = f"{q.topic}|{q.question}".encode("utf-8")
        import hashlib
        return hashlib.sha1(base).hexdigest()[:16]

    def show_question(self):
        if not self.session_questions:
            return
        q = self.session_questions[self.current]
        self.answered = False
        self.explanation.hide()
        self.topic_badge.setText(q.topic)
        self.diff_badge.setText(q.difficulty)
        self.question_label.setText(q.question)

        # Shuffle answers again at runtime; never train answer-position memory.
        pairs = [(answer, idx == q.correct_index) for idx, answer in enumerate(q.answers)]
        random.shuffle(pairs)
        self.current_display_answers = pairs

        labels = ("(A)", "(B)", "(C)", "(D)")
        for i, btn in enumerate(self.answer_buttons):
            btn.setText(f"{labels[i]} {pairs[i][0]}")
            btn.setEnabled(True)
            btn.set_state("normal")

        total = len(self.session_questions)
        self.status_line.setText(f"Question {self.current + 1} of {total}")
        self.progress_bar.setRange(0, max(total, 1))
        self.progress_bar.setValue(self.current + 1)
        self.prev_btn.setEnabled(total > 1)
        self.next_btn.setText("Next ->")

    def answer(self, display_index: int):
        if self.answered or not self.session_questions:
            return
        if display_index < 0 or display_index >= len(self.current_display_answers):
            return

        self.answered = True
        q = self.session_questions[self.current]
        selected_correct = self.current_display_answers[display_index][1]
        qid = self.question_id(q)

        correct_display = next(
            i for i, (_text, is_correct) in enumerate(self.current_display_answers) if is_correct
        )

        for i, btn in enumerate(self.answer_buttons):
            btn.setEnabled(False)
            if i == correct_display:
                btn.set_state("correct")
            elif i == display_index:
                btn.set_state("wrong")
            else:
                btn.set_state("dim")

        if selected_correct:
            self.session_correct += 1
            self.result_label.setText("✓“ Correct")
            missed = set(self.progress.get("missed", []))
            missed.discard(qid)
            self.progress["missed"] = sorted(missed)
        else:
            self.session_wrong += 1
            self.result_label.setText("X Not quite")
            missed = set(self.progress.get("missed", []))
            missed.add(qid)
            self.progress["missed"] = sorted(missed)

        attempts = self.progress.setdefault("attempts", {})
        rec = attempts.setdefault(qid, {"correct": 0, "wrong": 0})
        rec["correct" if selected_correct else "wrong"] += 1
        self.save_progress()

        self.reason_label.setText(q.reason)
        self.explanation.show()
        self.refresh_score()

    def refresh_score(self):
        self.score_chip.setText(
        f"{self.session_correct} correct • {self.session_wrong} wrong"
        )

    def next_question(self):
        if not self.session_questions:
            return
        self.current = (self.current + 1) % len(self.session_questions)
        self.show_question()

    def previous_question(self):
        if not self.session_questions:
            return
        self.current = (self.current - 1) % len(self.session_questions)
        self.show_question()

    # ---------- Progress ----------
    def load_progress(self) -> dict:
        try:
            if PROGRESS_FILE.exists():
                data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    return data
        except Exception:
            pass
        return {"missed": [], "attempts": {}}

    def save_progress(self):
        try:
            PROGRESS_FILE.write_text(
                json.dumps(self.progress, indent=2), encoding="utf-8"
            )
        except Exception:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName(APP_TITLE)
    window = StudyWindow()
    window.show()
    sys.exit(app.exec())
