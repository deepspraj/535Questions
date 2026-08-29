"""Chunking utilities."""

from .chunking_methods._recursive_chunker import _recursive_character_text_splitter


class Chunker:
    """Class to handle text chunking operations."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the Chunker instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        return None

    def recursive_chunker(
        self, pages: str, chunk_size=1000, chunk_overlap=100, *args, **kwargs
    ) -> list[str]:
        """Recursively chunk text into smaller segments.

        Args:
            pages (list[dict]): List of page dictionaries containing text to be chunked.
            chunk_size (int): Maximum size of each chunk in characters.
            chunk_overlap (int): Number of overlapping characters between consecutive chunks.
            *args: Unused positional arguments retained for compatibility.
            **kwargs: Unused keyword arguments retained for compatibility.

        Returns:
            list[str]: List of chunked text strings.

        """
        if not pages:
            raise ValueError("No pages provided for chunking. Please provide text to chunk.")

        return _recursive_character_text_splitter(pages, chunk_size, chunk_overlap, *args, **kwargs)
