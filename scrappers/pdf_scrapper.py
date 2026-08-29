"""Utilities for working with PDF files."""

import pymupdf


class PDFScraper:
    """Scrape text from PDF files.

    This class exposes simple methods for reading a PDF and collecting text
    from its pages. It can return either one combined string or a per-page
    list of dictionaries, optionally including page metadata.

    Attributes:
        path (str): Path to the PDF file used when no explicit path is passed.


    """

    def __init__(self, path: str = None, *args, **kwargs):
        """Store the default PDF path used by the scraper.

        Args:
            path (str): Path to the PDF file.
            *args: Unused positional arguments retained for compatibility.
            **kwargs: Unused keyword arguments retained for compatibility.

        """
        self.path = path
        return None

    def scrape_pdf_pagewise(
        self, path: str = None, metadata_needed: bool = False, *args, **kwargs
    ) -> list[dict]:
        """Extract text for each page in a PDF.

        If a path is provided, it is used for this call; otherwise the instance
        path is used. Each page is added to a list as a dictionary containing the
        page number and extracted text. When metadata_needed is true, the
        dictionary also includes the page width, height, and raw text blocks.

        Args:
            path: Path to the PDF file. If omitted, uses the instance path.
            metadata_needed: Whether to include page dimensions and block metadata.
            *args: Unused positional arguments retained for compatibility.
            **kwargs: Unused keyword arguments retained for compatibility.

        Returns:
            A list of page dictionaries. Each item contains at least the
            "page_number" and "text" keys. When metadata_needed is true, it also
            includes "width", "height", and "blocks".

        """
        if not self.path and not path:
            raise ValueError("No PDF path provided. Please specify a path.")

        # Use the explicit path when one is supplied; otherwise fall back to the instance path.
        if not path:
            path = self.path

        # Open the PDF document.
        doc = pymupdf.open(path)

        pages = []

        # Iterate over each page and collect the text for that page.
        for page_number, page in enumerate(doc, start=1):
            page_data = {"page_number": page_number, "text": page.get_text()}

            if metadata_needed:
                page_data.update(
                    {
                        "width": page.rect.width,
                        "height": page.rect.height,
                        "blocks": page.get_text("dict")["blocks"],
                    }
                )

            pages.append(page_data)

        # Close the document to release resources.
        doc.close()

        return pages

    def scrape_pdf(self, path: str = None, *args, **kwargs) -> str:
        """Combine the text from all pages in a PDF into a single string.

        If a path is provided, it is used for this call; otherwise the instance
        path is used. The method concatenates the extracted text from each page
        into one string and returns it.

        Args:
            path: Path to the PDF file. If omitted, uses the instance path.
            *args: Unused positional arguments retained for compatibility.
            **kwargs: Unused keyword arguments retained for compatibility.

        Returns:
            A single string containing the concatenated text from all pages.

        """
        if not self.path and not path:
            raise ValueError("No PDF path provided. Please specify a path.")

        # Use the explicit path when one is supplied; otherwise fall back to the instance path.
        if not path:
            path = self.path

        # Open the PDF document.
        doc = pymupdf.open(path)

        pages = ""

        # Iterate over each page and append its text to the accumulated string.
        for page in doc:
            pages += page.get_text()

        # Close the document to release resources.
        doc.close()

        return pages
