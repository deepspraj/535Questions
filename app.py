"""Application entry point."""

from dotenv import dotenv_values

from chunkers import Chunker
from config.config import WorkingDirectory
from embedders import Embedder
from scrappers import PDFScraper
from vectorstore import VectorStore

if __name__ == "__main__":
    # Set Root folder as current working directory
    wd = WorkingDirectory()
    wd.set_cwd()

    # Load env specific values
    envkeys = dotenv_values(".env")

    abs_file_path = wd.cwd() + "\\data\\test\\"
    file_name = "meditations.pdf"

    scrapper = PDFScraper(abs_file_path + file_name)
    chunker = Chunker()
    vdb = VectorStore()
    vdb_test_coll = vdb.create_collection("test1")

    pages = scrapper.scrape_pdf()
    chunks = chunker.recursive_chunker(pages)
    embedder = Embedder(
        envkeys["EMBEDDING_MODEL"],
        envkeys["EMBEDDING_MODEL_API_KEY"],
        envkeys["EMBEDDING_SERVICE_PROVIDER"],
    )

    embedder.save_embed_to_store(
        chunks=chunks,
        file_name=file_name,
        file_path=abs_file_path,
        db_coll=vdb_test_coll,
    )
