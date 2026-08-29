"""Application entry point."""

from dotenv import dotenv_values

from chunkers import Chunker
from config.config import set_cwd
from scrappers import PDFScraper

if __name__ == "__main__":
    # Set Root folder as current working directory
    set_cwd()

    # Load env specific values
    envkeys = dotenv_values(".env")

    scrapper = PDFScraper("data\\Constitutions\\USA\\ConstitutionOfUSA.pdf")
    chunker = Chunker()

    pages = scrapper.scrape_pdf()
    chunks = chunker.recursive_chunker(pages)
