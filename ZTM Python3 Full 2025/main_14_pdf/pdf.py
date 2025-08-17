from pypdf import PdfReader, PdfWriter
import os

# Paths to PDF files
pdf_dummy_path = os.path.join(os.path.dirname(__file__), "dummy.pdf")
pdf_twopages_path = os.path.join(os.path.dirname(__file__), "twopages.pdf")
pdf_rotated_dummy_path = os.path.join(
    os.path.dirname(__file__), "rotated_dummy.pdf")
pdf_combined_path = os.path.join(os.path.dirname(__file__), "combined.pdf")
pdf_watermark_path = os.path.join(os.path.dirname(__file__), "wtr.pdf")
pdf_output_watermarked = os.path.join(
    os.path.dirname(__file__), "watermarked_output.pdf")

# Rotate first page of dummy.pdf
with open(pdf_dummy_path, 'rb') as file:
    reader = PdfReader(file)
    writer = PdfWriter()
    page = reader.pages[0]
    page.rotate(90)  # rotate 90 degrees clockwise
    writer.add_page(page)
    with open(pdf_rotated_dummy_path, 'wb') as output_file:
        writer.write(output_file)

# Combine PDFs into one


def pdf_combiner(pdf_list, output_path):
    merger = PdfWriter()
    for pdf in pdf_list:
        if os.path.exists(pdf):
            print(f"Adding {pdf}...")
            merger.append(pdf)
        else:
            print(f"File {pdf} does not exist.")
    merger.write(output_path)
    merger.close()


pdf_combiner([pdf_dummy_path, pdf_twopages_path], pdf_combined_path)

# Add watermark to combined PDF


def add_watermark(input_pdf, watermark_pdf, output_pdf):
    with open(input_pdf, 'rb') as in_file, open(watermark_pdf, 'rb') as wtr_file:
        input_reader = PdfReader(in_file)
        watermark_reader = PdfReader(wtr_file)
        writer = PdfWriter()

        watermark_page = watermark_reader.pages[0]

        for page in input_reader.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        with open(output_pdf, 'wb') as out_file:
            writer.write(out_file)


add_watermark(pdf_combined_path, pdf_watermark_path, pdf_output_watermarked)
