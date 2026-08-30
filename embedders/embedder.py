"""Embedder module."""


class Embedder:
    """Base class for Embedders."""

    def __init__(
        self,
        model_name: str = None,
        api_key: str = None,
        service_provier: str = None,
        *args,
        **kwargs,
    ) -> bool:
        """Initialize the Embedder instance.

        Args:
            model_name (str, optional): Name of the embedding model.
            api_key (str, optional): API key for the service provider.
            service_provier (str, optional): Name of the service provider.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            bool: True upon successful initialization.

        """
        if not model_name:
            raise ValueError("No Embedding Model Name was provided.")
        if not api_key:
            raise ValueError("API Key not provided")
        if not service_provier:
            raise ValueError("No Embedding Service Provider name provided.")

        self.model_name = model_name

        return True

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
            return self._google_authenticator(model_name, api_key, provider, *args, **kwargs)

        elif "groq" in provider.lower():
            return self._groq_authenticator(model_name, api_key, provider, *args, **kwargs)

        elif "claude" in provider.lower():
            return self._claude_authenticator(model_name, api_key, provider, *args, **kwargs)

        elif "openai" in provider.lower():
            return self._openai_authenticator(model_name, api_key, provider, *args, **kwargs)

        else:
            raise ValueError(
                "Currently the embedder supports Gemini, Groq and Claude. "
                "Please choose either of this."
            )

        return False

    def _google_authenticator(self, *args, **kwargs) -> bool:
        """Authenticate with Google."""
        raise NotImplementedError("Google authenticator not implemented.")

    def _groq_authenticator(self, *args, **kwargs) -> bool:
        """Authenticate with Groq."""
        raise NotImplementedError("Groq authenticator not implemented.")

    def _claude_authenticator(self, *args, **kwargs) -> bool:
        """Authenticate with Claude."""
        raise NotImplementedError("Claude authenticator not implemented.")

    def _openai_authenticator(self, *args, **kwargs) -> bool:
        """Authenticate with OpenAI."""
        raise NotImplementedError("OpenAI authenticator not implemented.")

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

    def embed(self, chunk, *args, **kwargs) -> dict[str, list[float]]:
        """Generate embeddings for a chunk of text.

        Args:
            chunk (str): The text chunk to embed.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            dict[str, list[float]]: The generated embeddings.

        """
        return None
