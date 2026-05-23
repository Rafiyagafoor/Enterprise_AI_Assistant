from pypdf import PdfReader


def extract_text(
    pdf_path
):

    text=""

    pdf=PdfReader(
        pdf_path
    )

    for page in pdf.pages:

        page_text=page.extract_text()

        if page_text:
            text+=page_text

    return text