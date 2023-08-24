# -*- coding: utf-8 -*-
"""
Load mods from path

Handles the ``resources`` directory
"""
from pathlib import Path
from typing import Callable


class RessourcesLoader:
    """Main object for loading ressources."""

    def __init__(self, path: Path) -> None:
        """Initialize the mod loader.

        :param Path path: Path to the ressources folder.
            Default: ``resources``.
        """
        self.path: Path = path

    @staticmethod
    def _check_dir(path: Path, ressource: str) -> None:
        """Check if a path is a directory.

        :param Path path: Directory.
        :param str ressource: Ressource in the error message.
        """
        if not path.is_dir():
            raise FileNotFoundError(f"{ressource} is not a directory")

    def _load_ressource(self, name: str, callback: Callable[[Path], None]) -> None:
        """Load ressources.

        :param str name: Ressource to load.
            Also the name of the ressource folder.
        :param Callable[[Path], None] callback: Function to load the ressource
        """
        folder: Path = self.path / name
        self._check_dir(folder, name)
        for element in folder.iterdir():
            if not element.is_dir() or element.suffix != ".zip":
                raise TypeError(f"{name} {element.name} is not in a standard format")
            callback(element)
