# Python PyQt5 Digital Clock

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


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
        self.time_label.setStyleSheet("font-size: 90px;" "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color:black;" "margin: 0px;" "padding: 0px")

        font_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "assets", "DigitalDystopia-mL5ma.ttf"
            )
        )
        if not os.path.exists(font_path):
            print(f"Error: Font file not found at {font_path}")
            return

        font_id = QFontDatabase.addApplicationFont(
            font_path
        )  # Class - querying fonts to the app
        font_family = QFontDatabase.applicationFontFamilies(font_id)[
            0
        ]  # Add font_id to app font families
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

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
