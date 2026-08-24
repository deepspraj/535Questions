"""Application entry point."""

from dotenv import dotenv_values

from config.config import set_cwd
from scrappers import scrape_pdf

if __name__ == "__main__":
    # Set Root folder as current working directory
    set_cwd()

    # Load env specific values
    envkeys = dotenv_values(".env")

    pages = scrape_pdf("data\\Constitutions\\USA\\ConstitutionOfUSA.pdf")
