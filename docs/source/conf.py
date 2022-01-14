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

sphinxConfFile = os.path.abspath('../../sphinxConfig.yml')

with open(sphinxConfFile, "rt") as file_obj:
    sphinxParameters = yaml.safe_load(file_obj.read())

sys.path.insert(0, os.path.abspath('_ext'))
sys.path.insert(0, os.path.abspath('../../{}'.format(sphinxParameters['project']['scriptsFolder'])))

#sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = sphinxParameters['project']['name']
author = sphinxParameters['project']['authors']
copyright = '{}, {}'.format(str(sphinxParameters['project']['copyright']), author)

# The full version, including alpha/beta/rc tags
release = str(sphinxParameters['project']['release'])
version = 'v: {}'.format(release)

numfig = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.viewcode', 
              'sphinx.ext.autodoc', 
              'sphinx.ext.napoleon', 
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.mathjax', 
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

latex_logo = '_static/Pfizer_Logo_Color_RGB.png'


latex_elements = {}
# The paper size ('letterpaper' or 'a4paper').
latex_elements['papersize'] = 'letterpaper'
# The font size ('10pt', '11pt' or '12pt').
latex_elements['pointsize'] = '11pt'
# Remove white page after each chapter
latex_elements['extraclassoptions'] = r'''
openany, oneside
'''
latex_elements['figure_align'] = 'htbp'
# Additional stuff for the LaTeX preamble.
latex_elements['preamble'] = r'''
\usepackage{lastpage}
%% must wrap the whole latex in \makeatletter...\makeatother to use \py@HeaderFamily
\makeatletter

  \fancypagestyle{plain}{
    \fancyhf{}

    \fancyfoot[L]{}
    \fancyfoot[C]{Pfizer Internal Use}
    \fancyfoot[R]{Page {\py@HeaderFamily\thepage} of \textbf{\pageref*{LastPage}}}

    \fancyhead[L]{\includegraphics[width=2.5cm]{Pfizer_Logo_Color_RGB.png}}
    \fancyhead[C]{{\py@HeaderFamily \@title}}
    \fancyhead[R]{}

    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
  }

  \fancypagestyle{normal}{
    \fancyhf{}

    \fancyfoot[L]{}
    \fancyfoot[C]{Pfizer Internal Use}
    \fancyfoot[R]{Page {\py@HeaderFamily\thepage} of \textbf{\pageref*{LastPage}}}

    \fancyhead[L]{\includegraphics[width=2.5cm]{Pfizer_Logo_Color_RGB.png}}
    \fancyhead[C]{{\py@HeaderFamily \@title}}
    \fancyhead[R]{}

    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
  }
\makeatother

\usepackage{titlesec}
\titleformat{\chapter}{\huge\bfseries}{\thechapter. \hspace{2mm}}{0pt}{\huge}

%% spacing between line
\usepackage{setspace}
%\onehalfspacing
%\doublespacing
\singlespacing

%% datetime
\usepackage{datetime}

\newdateformat{MonthYearFormat}{%
    \monthname[\THEMONTH] \THEDAY, \THEYEAR}

\renewcommand{\releasename}{{\py@HeaderFamily \py@release}}
'''

latex_elements['maketitle'] = r'''
\pagenumbering{Roman} %% to avoid page 1 conflict with actual page 1

\begin{titlepage}
    %% must wrap the whole latex in \makeatletter...\makeatother to use \py@HeaderFamily
    \makeatletter
        
        \centering
        \vspace*{30mm} %% * is used to give space from top
        \textbf{\Huge{{\py@HeaderFamily \@title}}}
        
        \vspace{0mm}

        \Large \textbf{{\py@HeaderFamily \py@release}}
        \vspace{10mm}
        \begin{figure}[!h]
            \centering
            \includegraphics[scale=0.2]{Pfizer_Logo_Color_RGB.png}
        \end{figure}

        \vspace{10mm}
        \Large \textit{\textbf{{\py@HeaderFamily \@author}}}
        \vspace{5mm}

        \small  Last updated : \MonthYearFormat\today

        %% \vfill adds at the bottom
        \vfill
        \small \textit{Repository available at the following github:}
        \small \url{https://github.com/brentjm/Waters-Patrol-Connectivity}
    \makeatother
\end{titlepage}

'''

