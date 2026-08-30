"""Vector store management for embeddings."""

import chromadb

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
            self.dbpath = WorkingDirectory.cwd() + "\\data\\vectordb\\"
        else:
            self.dbpath = path
        self._create_db(self.dbpath)
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
        self.cdb_client = chromadb.PersistentClient(path=self.dbpath)
        print("ChromaDB Created")
        return True
