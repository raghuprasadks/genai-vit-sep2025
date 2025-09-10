import PyPDF2
import os
def upload_pdf(file):
    

    if file is None:
        return "No file uploaded."

    # Save the uploaded PDF file
    file_path = os.path.join("uploads", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    # Extract text from the PDF
    text = extract_text_from_pdf(file_path)
    
    return text

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text