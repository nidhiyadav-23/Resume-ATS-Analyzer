import fitz


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    try:
        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()
        return text.strip()

    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")