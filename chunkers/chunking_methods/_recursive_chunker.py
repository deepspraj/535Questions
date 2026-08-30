def _recursive_character_text_splitter(
    text: str, chunk_size: int = 1000, chunk_overlap: int = 200, *args, **kwargs
) -> list[str]:
    """Split a string into smaller overlapping chunks.

    This is the core logic that actually does the chopping. It takes a big
    string, figures out the chunk size and overlap, and cleanly slices it
    up into a list of smaller strings.

    Args:
        text: The giant input string we need to chunk.
        chunk_size: The max length for each chunk (default 1000).
        chunk_overlap: How many characters to overlap (default 200).
        *args: Extra positional args (ignored).
        **kwargs: Extra keyword args (ignored).

    Returns:
        A list of smaller, overlapping string chunks.

    Example:
        chunks = _recursive_character_text_splitter("Some huge text...")

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks: list[str] = []
    start = 0
    step = chunk_size - chunk_overlap
    total_length = len(text)

    while start < total_length:
        end = min(start + chunk_size, total_length)
        chunks.append(text[start:end])
        start += step

    return chunks
