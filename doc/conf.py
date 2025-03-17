# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# -- Project information --
project = "OC-Lettings"
copyright = "2025, Adev"
author = "Orange Country Letinngs, Adev"
release = "2.0.0"
language = "fr"

# Charger les variables d'environnement
dotenv_path = Path(__file__).resolve().parent.parent / ".env.local"
if dotenv_path.exists():
    print(f"Chargement des variables depuis {dotenv_path}")
    load_dotenv(dotenv_path)
else:
    print(f"⚠️ Fichier .env.local non trouvé : {dotenv_path}")

# Définition du chemin du projet Django
DJANGO_PROJECT_PATH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DJANGO_PROJECT_PATH))

# -- Définition du module de settings --
# On force la variable d'environnement pour être sûr qu'elle est définie
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
os.environ.setdefault("DATABASE_ENGINE", "sqlite3")
os.environ.setdefault("DATABASE_NAME", "oc-lettings-site.sqlite3")
# Debugging
print(f"sys.path = {sys.path}")
print(f"DJANGO_SETTINGS_MODULE = {os.environ.get('DJANGO_SETTINGS_MODULE')}")
print("### ENVIRONMENT VARIABLES (DEBUG) ###")
for key, value in os.environ.items():
    if "DATABASE" in key or "DEBUG" in key:
        print(f"{key} = {value}")

# -- Initialisation de Django --
try:
    import django

    django.setup()
    print("OK ! Django initialisé avec succès")
except Exception as e:
    print(f"❌Erreur lors de l'initialisation de Django: {e}")

# -- Extensions Sphinx --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # pour importer les modules qu'on documente
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",  # pour les docstrings google style
    "myst_parser",  # pour ajouter des .md
]
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "show-inheritance": True,
}
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options pour la sortie HTML --
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

#
# -- Paramètres Napoleon --
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
