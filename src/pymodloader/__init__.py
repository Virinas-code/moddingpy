# -*- coding: utf-8 -*-
"""
PyModLoader

Load mods for :py:mod:`moddingpy`
"""
from pathlib import Path

from .load import RessourcesLoader


def init(ressources_path: Path) -> None:
    """
    Initialize the mod loader.

    Loads mods.
    """
    loader: RessourcesLoader = RessourcesLoader(ressources_path)
    return loader
