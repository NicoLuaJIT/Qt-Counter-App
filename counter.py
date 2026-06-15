import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class ScoreApp(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Counter App")
        self.resize(400, 200)

        self.score_a = int(0)
        self.score_b = int(0)
        self.score_c = int(1)
        self.score_d = int(2)

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self) -> None:
        self.layout = QVBoxLayout()

        self.label_a = QLabel(f"Score A: {self.score_a}")
        self.label_b = QLabel(f"Score B: {self.score_b}")
        self.label_c = QLabel(f"Score C: {self.score_c}")
        self.label_d = QLabel(f"Score D: {self.score_d}")

        self.btn_a = QPushButton("Increment A")
        self.btn_b = QPushButton("Decrement B")
        self.btn_c = QPushButton("Double C")
        self.btn_d = QPushButton("Divide D")

        for widget in [self.label_a, self.label_b, self.label_c, self.label_d,
                       self.btn_a, self.btn_b, self.btn_c, self.btn_d]:
            self.layout.addWidget(widget)

        self.setLayout(self.layout)

    def connect_signals(self) -> None:
        self.btn_a.clicked.connect(self.increment_a)
        self.btn_b.clicked.connect(self.decrement_b)
        self.btn_c.clicked.connect(self.double_c)
        self.btn_d.clicked.connect(self.divide_d)

    def increment_a(self) -> None:
        self.score_a += 1
        self.label_a.setText(f"Score A: {self.score_a}")

    def decrement_b(self) -> None:
        self.score_b -= 1
        self.label_b.setText(f"Score B: {self.score_b}")

    def double_c(self) -> None:
        self.score_c *= 2
        self.label_c.setText(f"Score C: {self.score_c}")

    def divide_d(self) -> None:
        self.score_d /= 2
        self.label_d.setText(f"Score D: {self.score_d}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScoreApp()
    window.show()
    sys.exit(app.exec())