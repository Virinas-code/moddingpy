# -*- coding: utf-8 -*-
"""
Load mods from path

Handles the ``resources`` directory
"""
from pathlib import Path


class RessourcesLoader:
    """Main object for loading ressources."""

    def __init__(self, path: Path) -> None:
        """Initialize the mod loader.

        :param Path path: Path to the ressources folder.
            Default: ``resources``.
        """
        self.path: Path = path
