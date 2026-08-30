"""Vector store management for embeddings."""

import chromadb
from chromadb.api.models.Collection import Collection

from config import WorkingDirectory


class VectorStore:
    """Handles vector database operations."""

    def __init__(self, path: str = None) -> None:
        """Initialize the VectorStore and create the database client.

        This sets up our ChromaDB connection. If you don't give it a path,
        it automatically figures out the default data directory and puts
        the database there for you.

        Args:
            path: An optional custom path to save the database.

        Returns:
            Nothing.

        Example:
            vdb = VectorStore()

        """
        if not path:
            print("Initializing on default path as no path was provided.")
            self.db_path = WorkingDirectory.cwd() + "\\data\\vectordb\\"
        else:
            self.db_path = path
        self._create_db(self.db_path)

        return None

    def _create_db(self, *args, **kwargs) -> bool:
        """Create the ChromaDB persistent client.

        This is an internal helper that actually spins up the ChromaDB
        client using the path we figured out in __init__.

        Args:
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            True once the client is successfully created.

        Example:
            self._create_db()

        """
        if WorkingDirectory.empty_dir(self.db_path):
            self.cdb_client = chromadb.PersistentClient(path=self.db_path)
            print("ChromaDB Created")
        else:
            print("Already Created")
        return True

    def _create_connection(self, *args, **kwargs) -> bool:
        """Force a fresh connection to the ChromaDB client.

        Sometimes the client hasn't been initialized yet when we try to
        use a collection. This just spins up a new PersistentClient at
        the configured path so everything else can work without crashing.

        Args:
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            True once the connection is successfully established.

        Example:
            self._create_connection()

        """
        self.cdb_client = chromadb.PersistentClient(path=self.db_path)
        return True

    def create_collection(self, doc_name: str, *args, **kwargs) -> Collection:
        """Create or retrieve a collection in the database.

        This checks if a collection with the given document name already
        exists in our ChromaDB. If it does, it simply grabs it. If it doesn't,
        it creates a fresh one for us to store our document embeddings in.

        Args:
            doc_name: The name of the collection (usually based on the document name).
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            The ChromaDB Collection object ready for use.

        Example:
            collection = vdb.create_collection("us_constitution")

        """
        if not hasattr(self, "cdb_client") or not self.cdb_client:
            self._create_connection()

        return self.cdb_client.get_or_create_collection(name=doc_name)

    def delete_collection(self, doc_name: str, *args, **kwargs) -> Collection:
        """Delete a collection from the database.

        If you're done with a collection or need to wipe it clean, this
        will completely remove it from ChromaDB.

        Args:
            doc_name: The name of the collection you want to obliterate.
            *args: Extra positional args (ignored).
            **kwargs: Extra keyword args (ignored).

        Returns:
            Nothing (though it's typed to return Collection).

        Example:
            vdb.delete_collection("us_constitution")

        """
        if not hasattr(self, "cdb_client") or not self.cdb_client:
            self._create_connection()

        return self.cdb_client.delete_collection(name=doc_name)
