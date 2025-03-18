# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

import django

# -- Project information --
project = "OC-Lettings"
copyright = "2025, Adev"
author = "Orange Country Letinngs, Adev"
release = "2.0.0"

# Désactiver Sentry
os.environ["SENTRY_DSN"] = ""
sys.path.insert(0, os.path.abspath(".."))
os.environ["DJANGO_SETTINGS_MODULE"] = "oc_lettings_site.settings"
django.setup()

# -- Extensions Sphinx --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # pour importer les modules qu'on documente
    "sphinx.ext.viewcode",  # pour ajout des liens vers le code source (coloration syntaxique etc)
    "sphinx.ext.napoleon",  # pour les docstrings google style
    "myst_parser",  # pour ajouter des .md
    "sphinx.ext.autosummary",  # générer un tableau des routes
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
language = "fr"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/urls.py"]

# -- Options pour la sortie HTML --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Paramètres autodoc --
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "exclude-members": "*",
    "show-inheritance": True,
}

# -- Paramètres napoleon --
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
