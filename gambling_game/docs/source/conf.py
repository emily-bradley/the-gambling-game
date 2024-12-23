# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Gambling Game'
copyright = '2023, Emily Kenney'
author = 'Emily Kenney'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_mdinclude',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.confluencebuilder',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Confluence --
confluence_publish = True
confluence_space_key = 'DSCOP'
confluence_ask_password = True
# (for Confluence Cloud)
confluence_server_url = 'https://standard.atlassian.net/wiki/'
confluence_server_user = 'emily.kenney@standard.com'
confluence_parent_page = 'The Gambling Game'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
