"""Utility functions for configuring the application working directory."""

import os
from pathlib import Path


def set_cwd(*args, **kwargs) -> str:
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

    # Verify the change
    print(f"New Working Directory: {os.getcwd()}")

    return os.getcwd()
