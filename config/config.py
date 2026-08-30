"""Utility functions for configuring the application working directory."""

import os
from pathlib import Path


class WorkingDirectory:
    """Manages the application's working directory."""

    def __init__(self, path: str = None, *args, **kwargs) -> None:
        """Set up the working directory manager.

        This just initializes the class. We don't actually do much here yet,
        but it gives us a clean slate to work with directory paths.

        Args:
            path: An optional path string if you want to override the default.
            *args: Extra positional arguments (ignored).
            **kwargs: Extra keyword arguments (ignored).

        Returns:
            Nothing. It just sets up the object.

        Example:
            wd = WorkingDirectory()

        """
        return None

    def set_cwd(self, *args, **kwargs) -> str:
        """Set the project root folder as the current working directory.

        This function sets the root folder as the current working directory
        so that downstream files can use relative file paths with respect
        to the project root.

        Args:
            *args: Additional positional arguments. Not used.
            **kwargs: Additional keyword arguments. Not used.

        Returns:
            The path to the root folder as a string.

        Example:
            set_cwd()

        """
        # Get the absolute path of the current script
        script_path = Path(__file__).resolve()

        # Go up to the root folder path
        root_dir = script_path.parent.parent

        # Change the current working directory to the root
        os.chdir(root_dir)

        return os.getcwd()

    @staticmethod
    def cwd(*args, **kwargs) -> str:
        """Grab the current working directory.

        Just a quick helper function to spit out the current directory path
        we're running in, so we don't have to keep importing os everywhere.

        Args:
            *args: Extra positional arguments (ignored).
            **kwargs: Extra keyword arguments (ignored).

        Returns:
            The absolute path of wherever we currently are as a string.

        Example:
            current_path = WorkingDirectory.cwd()

        """
        return os.getcwd()
