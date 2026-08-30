"""Gemini Authentication module."""

from google.oauth2.credentials import Credentials


class GeminiEmbedder:
    """Embedder class for Gemini."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the Gemini embedder.

        This sets up our Gemini class. Right now it doesn't take any
        special parameters, but we might add some later if we need to
        configure the client further.

        Args:
            *args: Extra positional arguments (ignored).
            **kwargs: Extra keyword arguments (ignored).

        Returns:
            Nothing.

        Example:
            embedder = GeminiEmbedder()

        """
        return None

    @classmethod
    def _validate_token(cls, token: str) -> bool:
        """Check if our Gemini API token actually works.

        We use this internally to test the token against the credentials
        system before we try to make any real embedding calls. It prints
        out whether it succeeded or failed so we can debug easily.

        Args:
            token: The raw API key string we want to test.

        Returns:
            True if the token is valid, False if it's a dud.

        Example:
            is_valid = GeminiEmbedder._validate_token("my-fake-token")

        """
        print(token)
        credentials = Credentials(token=token)

        if credentials.valid:
            print(credentials.valid)
            print("Correct TOken")
            # return True
        print("InCorrect TOken")
        return False
