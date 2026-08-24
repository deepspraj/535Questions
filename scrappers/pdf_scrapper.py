"""Utilities for extracting content from PDF files."""

import pymupdf


def scrape_pdf(path: str, *args, **kwargs) -> list:
    """Extract structured content from a PDF file.

    This function opens a PDF file and extracts information from each
    page, including the page number, page dimensions, and text blocks.
    The extracted blocks retain the structure provided by PyMuPDF.

    Args:
        path: Path to the PDF file.
        *args: Additional positional arguments. Not used.
        **kwargs: Additional keyword arguments. Not used.

    Returns:
        A list of dictionaries, where each dictionary contains the
        page number, page width, page height, and extracted text blocks.

    Example:
        pages = scrape_pdf("data/Constitutions/USA/ConstitutionOfUSA.pdf")

    """
    # Open the PDF document
    doc = pymupdf.open(path)

    pages = []

    # Iterate through each page and print the text
    for page_number, page in enumerate(doc, start=1):
        page_data = {
            "page_number": page_number,
            "width": page.rect.width,
            "height": page.rect.height,
            "blocks": page.get_text("dict")["blocks"],
        }

        pages.append(page_data)

    # Close the document to free up memory
    doc.close()

    return pages
