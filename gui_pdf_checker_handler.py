import os
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

# Debugging: Print Python executable path
print(f"Python executable: {sys.executable}")

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("Error: 'python-dotenv' is not installed. Please install it using 'pip install python-dotenv'.")
    sys.exit(1)

# Load environment variables from .env file
load_dotenv()

# Define the output folder path from the .env file
output_folder = os.getenv('OUTPUT_FOLDER_FOR_COMBINED_FILE')

# Define the path to the explanation text file
explanation_file_path = "gui_explanation.txt"

class PDFToolsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("PDF Handler GUI")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        # Apply dark mode stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;  /* Dark blue background */
                color: #FFFFFF;  /* White text */
            }
            QPushButton {
                background-color: #4C566A;  /* Dark purple button background */
                color: #FFFFFF;  /* White text */
                border: 2px solid #5E81AC;  /* Light blue border */
                border-radius: 10px;  /* Rounded corners */
                padding: 10px;  /* Padding inside buttons */
                font-size: 14px;  /* Font size */
            }
            QPushButton:hover {
                background-color: #5E81AC;  /* Light blue background on hover */
            }
            QPushButton:pressed {
                background-color: #81A1C1;  /* Lighter blue background when pressed */
            }
            QMessageBox {
                background-color: #2E3440;  /* Dark blue background */
                color: #FFFFFF;  /* White text */
            }
            QMessageBox QLabel {
                color: #FFFFFF;  /* White text */
            }
            QMessageBox QPushButton {
                background-color: #4C566A;  /* Dark purple button background */
                color: #FFFFFF;  /* White text */
                border: 2px solid #5E81AC;  /* Light blue border */
                border-radius: 5px;  /* Rounded corners */
                padding: 5px;  /* Padding inside buttons */
                font-size: 12px;  /* Font size */
            }
            QMessageBox QPushButton:hover {
                background-color: #5E81AC;  /* Light blue background on hover */
            }
            QMessageBox QPushButton:pressed {
                background-color: #81A1C1;  /* Lighter blue background when pressed */
            }
        """)

        # Create buttons
        self.button1 = QPushButton("Run PDF Unlocking Script", self)
        self.button2 = QPushButton("Run PDF Combining Script", self)
        self.button3 = QPushButton("Open Output Folder", self)
        self.button4 = QPushButton("Open Explanation File", self)

        # Connect buttons to their respective functions
        self.button1.clicked.connect(self.run_pdf_unlocking)
        self.button2.clicked.connect(self.run_pdf_combining)
        self.button3.clicked.connect(self.open_output_folder)
        self.button4.clicked.connect(self.open_explanation_file)

        # Create a vertical layout and add buttons to it
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        # Set the layout for the window
        self.setLayout(layout)

    def run_pdf_unlocking(self):
        """Run the PDF unlocking script"""
        try:
            subprocess.run([sys.executable, "pdf_saver_unlocking_files.py"], check=True)
            QMessageBox.information(self, "Success", "PDF unlocking script executed successfully!")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to run PDF unlocking script: {e}")

    def run_pdf_combining(self):
        """Run the PDF combining script"""
        try:
            subprocess.run([sys.executable, "pdf_combined_to_1_file.py"], check=True)
            QMessageBox.information(self, "Success", "PDF combining script executed successfully!")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to run PDF combining script: {e}")

    def open_output_folder(self):
        """Open the output folder"""
        if os.path.exists(output_folder):
            if sys.platform == "win32":
                os.startfile(output_folder)  # Open folder in Windows
            elif sys.platform == "darwin":
                subprocess.run(["open", output_folder])  # Open folder in macOS
            else:
                subprocess.run(["xdg-open", output_folder])  # Open folder in Linux
        else:
            QMessageBox.critical(self, "Error", f"Output folder not found: {output_folder}")

    def open_explanation_file(self):
        """Open the explanation text file"""
        if os.path.exists(explanation_file_path):
            if sys.platform == "win32":
                os.startfile(explanation_file_path)  # Open file in Windows
            elif sys.platform == "darwin":
                subprocess.run(["open", explanation_file_path])  # Open file in macOS
            else:
                subprocess.run(["xdg-open", explanation_file_path])  # Open file in Linux
        else:
            QMessageBox.critical(self, "Error", f"Explanation file not found: {explanation_file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFToolsGUI()
    window.show()
    sys.exit(app.exec_())