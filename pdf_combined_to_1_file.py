import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

# Define the path to the folder containing the PDFs to combine
input_folder = os.getenv('OUTPUT_FOLDER_PATH_UNLOCKED_FILES')
# Define the path to the output folder where the combined PDF will be saved
output_folder = os.getenv('OUTPUT_FOLDER_FOR_COMBINED_FILE')
# Define the name of the output PDF file
output_filename = "combined_file.PDF"


def create_watermark(content):
    """Create a PDF page with text content to use as a watermark"""
    from reportlab.lib.pagesizes import letter  # Moved inside the function
    from io import BytesIO
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(100, 100, content)  # Position the text at x=100, y=100
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    watermark_page = new_pdf.pages[0]  # Renamed to avoid shadowing
    return watermark_page


# Create a PDF writer object
writer = PdfWriter()

# Iterate over each file in the input folder
for filename in tqdm(os.listdir(input_folder)):
    if filename.endswith('.PDF'):
        file_path = os.path.join(input_folder, filename)
        reader = PdfReader(file_path)
        watermark = create_watermark(filename)  # Create a watermark page for this filename
        # Add each page of the current PDF to the writer object
        for page in reader.pages:
            page.merge_page(watermark)  # Apply the watermark
            writer.add_page(page)

# Save the combined PDF to the output folder
output_path = os.path.join(output_folder, output_filename)
with open(output_path, "wb") as f:
    writer.write(f)

print(f"All PDFs combined into {output_path}")
