# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from typing import Any

print(os.getcwd())
sys.path.append(os.path.abspath("../../src"))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ModdingPy"
copyright = "2023, Virinas-code"
author = "Virinas-code"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# -- User settings -----------------------------------------------------------
autodoc_default_options: dict[str, Any] = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "special-members": True,
    "exclude-members": "__dict__, __module__, __weakref__",
}
