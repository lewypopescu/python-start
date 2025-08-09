import PyPDF2
import os

pdf_dummy_path = os.path.join(os.path.dirname(
    __file__), "dummy.pdf")

pdf_twopages_path = os.path.join(os.path.dirname(
    __file__), "twopages.pdf")

pdf_rotated_dummy_path = os.path.join(os.path.dirname(
    __file__), "rotated_dummy.pdf")

with open(pdf_dummy_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(f"Number of pages, dummy.pdf: {len(reader.pages)}")

with open(pdf_twopages_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(f"Number of pages, twopages.pdf: {len(reader.pages)}")

with open(pdf_dummy_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]  # Get the first page
    page.rotate(90)  # Rotate the page 90 degrees clockwise
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)  # Add the rotated page to the writer
    with open(pdf_rotated_dummy_path, 'wb') as output_file:
        writer.write(output_file)
