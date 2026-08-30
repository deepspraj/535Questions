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

        Just sets up the scraper. You can give it a PDF path now, or you
        can wait and pass the path directly to the scraping methods later.

        Args:
            path: An optional default path to a PDF file.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            Nothing.

        Example:
            scraper = PDFScraper("my_document.pdf")

        """
        self.path = path
        return None

    def scrape_pdf_pagewise(
        self, path: str = None, metadata_needed: bool = False, *args, **kwargs
    ) -> list[dict]:
        """Extract text from a PDF, keeping each page separate.

        This goes through the PDF page by page and rips out the text.
        It returns a list where each item is a page, which is super handy if
        you want to track which page a piece of information came from.

        Args:
            path: An optional path if you want to override the default one.
            metadata_needed: Set this to True if you also want page dimensions.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            A list of dictionaries, where each dict has the text for one page.

        Example:
            pages = scraper.scrape_pdf_pagewise()

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
        """Extract all the text from a PDF into one giant string.

        This just rips through the entire PDF and jams all the text from
        every single page together into one big string. Great for when you
        don't care about page numbers and just want the raw text.

        Args:
            path: An optional path to override the default one.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            A single massive string containing all the text.

        Example:
            all_text = scraper.scrape_pdf()

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
