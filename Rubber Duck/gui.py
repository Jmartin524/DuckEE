from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
import pyttsx3

class RAGSystemApp(QMainWindow):
    def __init__(self, qa_chain):
        super().__init__()
        self.qa_chain = qa_chain
        self.tts_engine = None  # Lazy-load the TTS engine
        self.voice_enabled = False  # Voice is off by default
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('DuckEE')
        self.setGeometry(100, 100, 600, 500)

        # Set up layout and widgets
        layout = QVBoxLayout()

        # Add an image at the top (Rubber_duck.png, 250x250)
        self.image_label = QLabel(self)
        pixmap = QPixmap('Rubber_duck.png').scaled(250, 250, Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Query input
        self.query_entry = QLineEdit(self)
        self.query_entry.setPlaceholderText("Enter your query here")
        layout.addWidget(self.query_entry)
        self.query_entry.returnPressed.connect(self.run_query)  # Support Enter key submission

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.run_query)
        layout.addWidget(self.submit_button)

        # Toggle Voice button
        self.voice_toggle_button = QPushButton("Turn On Voice", self)
        self.voice_toggle_button.clicked.connect(self.toggle_voice)
        layout.addWidget(self.voice_toggle_button)

        # Result text box
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def run_query(self):
        query = self.query_entry.text()
        if not query:
            self.result_text.setPlainText("Please enter a query.")
        else:
            # Run the query against the QA chain
            result = self.qa_chain.run(query)
            self.type_text(result)
            if self.voice_enabled:
                self.speak_text(result)

    def type_text(self, text):
        """Function to display text with a typing effect."""
        self.result_text.clear()  # Clear previous text
        self.current_text = text
        self.char_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_char)
        self.timer.start(50)  # Set typing speed (50ms between each character)

    def display_next_char(self):
        """Displays the next character in the text area."""
        if self.char_index < len(self.current_text):
            self.result_text.insertPlainText(self.current_text[self.char_index])
            self.char_index += 1
        else:
            self.timer.stop()  # Stop the timer when done typing

    def toggle_voice(self):
        if self.voice_enabled:
            self.voice_enabled = False
            self.voice_toggle_button.setText("Turn On Voice")
        else:
            self.voice_enabled = True
            self.voice_toggle_button.setText("Turn Off Voice")
            if not self.tts_engine:
                self.initialize_tts()  # Lazy-load the TTS engine only when voice is turned on

    def initialize_tts(self):
        """Initialize the TTS engine."""
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('voice', 'com.apple.voice.compact.en-GB.Daniel')
        self.tts_engine.setProperty('rate', 160)  # Medium pace

    def speak_text(self, text):
        """Speak text using TTS if voice is enabled."""
        if self.tts_engine:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()

    def stop_speaking(self):
        """Stop speaking the current text."""
        if self.tts_engine:
            self.tts_engine.stop()  # Stop the TTS engine immediately
