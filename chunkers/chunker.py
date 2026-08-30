"""Chunking utilities."""

from .chunking_methods._recursive_chunker import _recursive_character_text_splitter


class Chunker:
    """Class to handle text chunking operations."""

    def __init__(self, *args, **kwargs) -> None:
        """Set up the chunker tool.

        Just a basic setup method for our Chunker class. We don't have any
        persistent state to track yet, but this gives us a place to put it
        if we need it later.

        Args:
            *args: Catch-all for extra positional args.
            **kwargs: Catch-all for extra keyword args.

        Returns:
            Nothing.

        Example:
            my_chunker = Chunker()

        """
        return None

    def recursive_chunker(
        self, pages: str, chunk_size=1000, chunk_overlap=100, *args, **kwargs
    ) -> list[str]:
        """Break down a massive block of text into manageable pieces.

        We take a big string (like an entire constitution) and chop it up
        into smaller chunks so we don't blow up the token limit of our
        embedding models. It also overlaps the chunks a bit so we don't
        lose context in the middle of a sentence.

        Args:
            pages: The big string of text we want to chop up.
            chunk_size: How big each chunk should be (default is 1000).
            chunk_overlap: How many characters should overlap between chunks (default is 100).
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            A nice clean list of text chunks.

        Example:
            chunks = chunker.recursive_chunker(my_text, chunk_size=500)

        """
        if not pages:
            raise ValueError("No pages provided for chunking. Please provide text to chunk.")

        return _recursive_character_text_splitter(pages, chunk_size, chunk_overlap, *args, **kwargs)
