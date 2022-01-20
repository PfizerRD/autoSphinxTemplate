# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import sphinx_rtd_theme
import yaml
from datetime import date

sphinxConfFile = os.path.abspath('../../sphinxConfig.yml')

with open(sphinxConfFile, "rt") as file_obj:
    sphinxParameters = yaml.safe_load(file_obj.read())

sys.path.insert(0, os.path.abspath('_ext'))
for folder in sphinxParameters['project']['scriptsFolders']:
    sys.path.insert(0, os.path.abspath('../../{}'.format(folder)))

#sys.setrecursionlimit(1500)

datestr = date.today().strftime("%d-%b-%Y")

# -- Project information -----------------------------------------------------
project = sphinxParameters['project']['name']
author = sphinxParameters['project']['authors']
copyright = '{}, {}'.format(str(sphinxParameters['project']['copyright']), author)

# The full version, including alpha/beta/rc tags
release = str(sphinxParameters['project']['release'])
version = 'v: {}'.format(release)

variables_to_export = [
    "author",
    "release",
    "datestr"
]
frozen_locals = dict(locals())
rst_epilog = '\n'.join(map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export))
del frozen_locals

numfig = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel',
              'sphinx_rtd_theme',
              'sphinx.ext.todo']


# napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,

    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
'navigation_depth': 4,
    'titles_only': False
}

html_show_sourcelink = False
html_logo = '_static/Pfizer_Logo_White_PMS.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['style.css']

html_sidebars = {}
html_sidebars['**'] = ['globaltoc.html', 'sourcelink.html', 'searchbox.html']
html_sidebars['using/windows'] = ['windowssidebar.html', 'searchbox.html']
