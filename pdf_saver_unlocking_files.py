from dotenv import load_dotenv
from tqdm import tqdm
import pikepdf
import os

# Load environment variables from .env file
load_dotenv()

# Folder where your password-protected PDFs are stored
input_folder = os.getenv('INPUT_FOLDER_PATH_LOCKED_FILES')
output_folder = os.getenv('OUTPUT_FOLDER_PATH_UNLOCKED_FILES')

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load the list of passwords from the .env file
# Passwords are stored as a comma-separated string in the .env file
passwords_str = os.getenv('PASSWORDS')
passwords = passwords_str.split(',') if passwords_str else []

# List to keep track of files that could not be processed
unprocessed_files = []

# Process each file in the directory
for filename in tqdm(os.listdir(input_folder)):
    if filename.endswith('.PDF'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        file_processed = False

        # Attempt to open the PDF with each password
        for password in passwords:
            try:
                # Use .strip() to remove any extra spaces
                with pikepdf.open(input_path, password=password.strip()) as pdf:
                    pdf.save(output_path)
                    print(f'Successfully processed {filename} with password: {password}')
                    file_processed = True
                    break  # Exit the loop if the correct password was found
            except pikepdf.PasswordError:
                print(f'Password {password} did not work for {filename}. Trying next...')
            except Exception as e:
                print(f'An error occurred with {filename}: {str(e)}')
                break  # Exit the loop if there is an error other than a password error

        if not file_processed:
            # If no password worked
            print(f'Failed to process {filename}: No valid password found.')
            unprocessed_files.append(filename)

print('All files have been processed.')
if unprocessed_files:
    print("Files that couldn't be processed:")
    for file in unprocessed_files:
        print(file)
