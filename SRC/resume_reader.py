import PyPDF2

def read_resume(file_path):
    text = ""

    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text
