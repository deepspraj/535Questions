"""Embedder module."""

from hashlib import md5

from chromadb.api.models.Collection import Collection

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

        This sets up the core embedding manager. It grabs your API key,
        the model name, and the provider you want to use, so it's ready
        to start vectorizing text later.

        Args:
            model_name: The specific model to use (like 'text-embedding-004').
            api_key: Your secret API key.
            service_provier: The provider's name (like 'gemini' or 'openai').
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            Nothing.

        Example:
            embedder = Embedder("text-embedding-004", "my-key", "gemini")

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

        This routes the API key to the correct provider's authentication
        method to make sure the token is actually valid before we try to
        use it. Right now, only Gemini is fully hooked up!

        Args:
            model_name: The embedding model name.
            api_key: Your secret API key.
            provider: The service provider to authenticate against.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            True if authentication succeeds, False otherwise.

        Example:
            is_valid = self._authenticator("model-name", "my-key", "gemini")

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

        Need to switch to a different embedding model on the fly? Use this
        to update the model name without having to recreate the whole class.

        Args:
            new_model_name: The new model string you want to switch to.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            True once the model has been updated.

        Example:
            self.model_update("new-embedding-model-v2")

        """
        if not new_model_name:
            raise ValueError(
                "New Embedding Model Name must be provided in order to update the model."
            )

        self.model_name = new_model_name

        return True

    def _create_client(self, *args, **kwargs) -> object:
        """Create the actual provider client.

        This internal method spins up the specific API client based on
        which provider you're using (like the google-genai Client).

        Args:
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            The initialized client object, or None if unsupported.

        Example:
            client = self._create_client()

        """
        if "gemini" in self.provider:
            from google import genai

            client = genai.Client(api_key=self.api_key)
            return client
        return None

    def embed(self, chunks: list[str], *args, **kwargs) -> dict[str, list[float]]:
        """Generate embeddings for a list of text chunks.

        This is the main event. It takes a list of text chunks, fires them
        off to the embedding provider, and returns a dictionary mapping each
        piece of text to its generated vector.

        Args:
            chunks: A list of text strings you want to embed.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            A dictionary where the keys are the text chunks and the values
            are the list of floats representing the embeddings.

        Example:
            vectors = embedder.embed(["Hello world", "Another chunk"])

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

    def save_embed_to_store(
        self,
        chunks: list[str],
        file_name: str,
        file_path: str,
        db_coll: Collection,
        *args,
        **kwargs,
    ) -> None:
        """Process and save chunks to the vector database.

        This loops through the chunks of text, calculates a quick MD5 hash
        to see if we've already saved it before, and if it's new, we hit the
        embedding API and store the result in ChromaDB with all its metadata.

        Args:
            chunks: A list of text strings we want to embed and save.
            file_name: The name of the file these chunks came from.
            file_path: The absolute path to the original file.
            db_coll: The ChromaDB Collection where we'll save the embeddings.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            Nothing.

        Example:
            embedder.save_embed_to_store(chunks, "doc.pdf", "/path/to", coll)

        """
        client = self._create_client()

        embeddings = {}

        for index, chunk in enumerate(chunks):
            chunk_hash = md5(chunk.encode("utf-8"), usedforsecurity=False).hexdigest()

            db_result = db_coll.get(ids=[chunk_hash], include=[])

            if db_result:
                print("already in db")
                continue

            result = client.models.embed_content(model=self.model_name, contents=chunk)

            db_coll.add(
                ids=[chunk_hash],
                documents=[chunk],
                embeddings=[result.embeddings[0].values],
                metadatas=[
                    {"file_path": file_path, "file_name": file_name, "chunk_index": index + 1}
                ],
            )

        return embeddings
