"""Embedder module."""

from .auth_methods.gemini import GeminiEmbedder


class Embedder:
    """Base class for Embedders."""

    def __init__(
        self,
        model_name: str = None,
        api_key: str = None,
        service_provier: str = None,
        *args,
        **kwargs,
    ) -> None:
        """Initialize the Embedder instance.

        Args:
            model_name (str, optional): Name of the embedding model.
            api_key (str, optional): API key for the service provider.
            service_provier (str, optional): Name of the service provider.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            None: No return upon successful initialization.

        """
        if not model_name:
            raise ValueError("No Embedding Model Name was provided.")
        if not api_key:
            raise ValueError("API Key not provided")
        if not service_provier:
            raise ValueError("No Embedding Service Provider name provided.")

        # self._authenticated = self._authenticator(model_name, api_key, service_provier)
        self.model_name = model_name
        self.api_key = api_key
        self.provider = service_provier.lower()
        self._authenticated = True

        return None

    def _authenticator(self, model_name, api_key, provider, *args, **kwargs) -> bool:
        """Authenticate with the specified provider.

        Args:
            model_name (str): Name of the embedding model.
            api_key (str): API key for the service provider.
            provider (str): Name of the service provider.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            bool: True if authentication is successful, False otherwise.

        """
        if "gemini" in provider.lower():
            return GeminiEmbedder._validate_token(api_key)

        elif "groq" in provider.lower():
            raise NotImplementedError("Groq authenticator is not implemented yet.")

        elif "claude" in provider.lower():
            raise NotImplementedError("Claude authenticator is not implemented yet.")

        elif "openai" in provider.lower():
            raise NotImplementedError("OpenAI authenticator is not implemented yet.")

        else:
            raise ValueError(
                "Currently the embedder supports Gemini, Groq, Claude and OpenAI. "
                "Please choose either of this."
            )

        return False

    def model_update(self, new_model_name, *args, **kwargs) -> bool:
        """Update the embedding model.

        Args:
            new_model_name (str): New name for the embedding model.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            bool: True if the model was updated.

        """
        if not new_model_name:
            raise ValueError(
                "New Embedding Model Name must be provided in order to update the model."
            )

        self.model_name = new_model_name

        return True

    def _create_client(self, *args, **kwargs) -> object:

        if "gemini" in self.provider:
            from google import genai

            client = genai.Client(api_key=self.api_key)
            return client
        return None

    def embed(self, chunks: list[str], *args, **kwargs) -> dict[str, list[float]]:
        """Generate embeddings for a chunk of text.

        Args:
            chunks (list[str]): The text chunks to embed.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            dict[str, list[float]]: The generated embeddings.

        """
        if not self._authenticated:
            raise ValueError(
                f"Please Authenticate the token before using embedding sevice of {self.provider}."
            )

        client = self._create_client()

        embeddings = {}

        for chunk in chunks:
            result = client.models.embed_content(model=self.model_name, contents=chunk)

            embedding_chunk = result.embeddings[0].values
            embeddings[chunk] = embedding_chunk

        return embeddings
