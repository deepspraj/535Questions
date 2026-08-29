def _recursive_character_text_splitter(
    text: str, chunk_size: int = 1000, chunk_overlap: int = 200, *args, **kwargs
) -> list[str]:
    """Split a string into smaller overlapping chunks.

    Args:
        text (str): Input text to chunk.
        chunk_size (int): Maximum length of each chunk.
        chunk_overlap (int): Number of characters shared between neighboring chunks.
        *args: Unused positional arguments retained for compatibility.
        **kwargs: Unused keyword arguments retained for compatibility.

    Returns:
        list[str]: A list of chunk strings.

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
