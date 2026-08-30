"""Gemini Authentication module."""

from google.oauth2.credentials import Credentials


class GeminiEmbedder:
    """Embedder class for Gemini."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the GeminiEmbedder."""
        return None

    @classmethod
    def _validate_token(cls, token: str) -> bool:
        """Validate the provided token."""
        print(token)
        credentials = Credentials(token=token)

        if credentials.valid:
            print(credentials.valid)
            print("Correct TOken")
            # return True
        print("InCorrect TOken")
        return False
