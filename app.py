"""Application entry point."""

from config.config import WorkingDirectory
from vectorstore import VectorStore

if __name__ == "__main__":
    # Set Root folder as current working directory
    wd = WorkingDirectory()
    wd.set_cwd()

    # # Load env specific values
    # envkeys = dotenv_values(".env")

    # scrapper = PDFScraper("data\\constitutions\\usa\\ConstitutionOfUSA.pdf")
    # chunker = Chunker()

    # pages = scrapper.scrape_pdf()
    # chunks = chunker.recursive_chunker(pages)
    # embedder = Embedder(
    #     envkeys["EMBEDDING_MODEL"],
    #     envkeys["EMBEDDING_MODEL_API_KEY"],
    #     envkeys["EMBEDDING_SERVICE_PROVIDER"],
    # )

    vdb = VectorStore()
