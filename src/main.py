# Python PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(
    QWidget
):  # Widget inheritence from PyQt5, initialise components and elements
    def __init__(self):  # Custom constructor
        super().__init__()  # Inherit QWidget constructor
        self.time_label = QLabel(self)

        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):  # Customize components and elements.
        self.setWindowTitle("Digital Clock")
        self.setGeometry(1600, 1000, 400, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size: 90px;" "font-family: Arial;" "color: hsl(111, 100%, 50%);"
        )
        self.setStyleSheet("background-color:black;" "margin: 0px;" "padding: 0px")

        # Connect timer.timeout to update_time function
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Send timeout signal every 1000 ms

        self.update_time()

    def update_time(self):  # Update time
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)


if __name__ == "__main__":  # Initialize program if launched standalone
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())  # Initialise event loop of app and handle events within it
