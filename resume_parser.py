import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF resume.
    """

    text = ""

    # Open PDF from in-memory stream
    pdf_document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    # Loop through each page
    for page in pdf_document:
        text += page.get_text()

    return text.strip()