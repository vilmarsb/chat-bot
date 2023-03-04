import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QPushButton


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)
        
        # Input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,350,480,50)
        
        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500,350,50,50)

        self.show()

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
