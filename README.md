# pdf-cracker-handler 📄📂🔐🔓💻
PDF management tool that unlocks password-protected PDFs, combines multiple PDFs into one with watermarks, and provides a user-friendly GUI for easy operation, all while securely managing sensitive data using environment variables.

This GUI provides a user-friendly interface to manage two main scripts for handling PDF files. Below is an explanation of each script and how to use the GUI:


---

### 1. PDF Unlocking Script
This script unlocks password-protected PDFs using a list of passwords provided in the `.env` file.

#### How It Works:
- The script reads PDF files from the folder specified in the `.env` file (`INPUT_FOLDER_PATH_LOCKED_FILES`).
- It attempts to unlock each PDF using the passwords listed in the `.env` file (`PASSWORDS`).
- Unlocked PDFs are saved to the folder specified in the `.env` file (`OUTPUT_FOLDER_PATH_UNLOCKED_FILES`).

#### Usage:
- Place your password-protected PDFs in the input folder.
- Make sure that the name of each PDF file is exactly as you want the watermark to be on it.
--Example: "Salary_February_2025".pdf
- Add the passwords to the `.env` file as a comma-separated list.
- Run the script to unlock the PDFs.

#### Demo .env file (should look like this):
INPUT_FOLDER_PATH_LOCKED_FILES=C:\Users\username\Desktop\payslips
OUTPUT_FOLDER_PATH_UNLOCKED_FILES=C:\Users\username\Desktop\no_password
PASSWORDS=password1,password2,password3
OUTPUT_FOLDER_FOR_COMBINED_FILE=C:\Users\username\Desktop\combined_file

- *In this case the user changed his passwords for the files and want to unlock all the files with his previews passwords as well.
---

### 2. PDF Combining Script
This script combines multiple unlocked PDFs into a single PDF file and adds a watermark to each page.

#### How It Works:
- The script reads unlocked PDFs from the folder specified in the `.env` file (`OUTPUT_FOLDER_PATH_UNLOCKED_FILES`).
- It creates a watermark for each PDF using the filename as the watermark text.
- The script combines all PDFs into a single file and saves it to the folder specified in the `.env` file (`OUTPUT_FOLDER_FOR_COMBINED_FILE`).

#### Usage:
- Ensure the unlocked PDFs are in the correct folder.
- Run the script to combine the PDFs and add watermarks.

---

### 3. PDF Handler GUI
The GUI provides an easy way to run the above scripts and manage the output files.

#### Features:
- **Run PDF Unlocking Script**: Executes the PDF unlocking script.
- **Run PDF Combining Script**: Executes the PDF combining script.
- **Open Output Folder**: Opens the folder where the combined PDF is saved.
- **Open Explanation File**: Opens this text file for additional information.

#### Usage:
- Use the buttons in the GUI to run the scripts or open folders/files.
- Ensure the `.env` file is properly configured with the correct folder paths and passwords.

---

### Folder Structure
- **Input Folder for Locked Files**: Contains password-protected PDFs.
- **Output Folder for Unlocked Files**: Stores unlocked PDFs.
- **Output Folder for Combined File**: Stores the final combined PDF.

---

### Requirements
- Python 3.x
- Required Python packages: `PyPDF2`, `pikepdf`, `reportlab`, `python-dotenv`, `tqdm`, `PyQt5`

---

### Notes
- pip install -r requirements.txt
- Ensure the `.env` file is correctly configured with the required paths and passwords.
- Add the `.env` file to `.gitignore` to avoid exposing sensitive information.
- The GUI uses a dark theme for a modern and professional look.
---

For any issues or questions, refer to the documentation or contact the developer.
