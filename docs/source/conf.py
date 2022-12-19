# pylint: disable=redefined-builtin, invalid-name
# -*- coding: utf-8 -*-
"""
AiiDA-VASP documentation build configuration file, created by
sphinx-quickstart on Mon Feb 12 09:24:45 2018.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""
import datetime
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys

sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax',
    'sphinx.ext.viewcode', 'aiida.sphinxext'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AiiDA-VASP'
copyright = f'{datetime.datetime.now().year}, AiiDA-VASP development team'
author = 'AiiDA_VASP development team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
# release = u'0.2.4'
release = re.sub('^v', '', os.popen('git describe').read().strip())
version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
#exclude_patterns = ['_build', 'api/aiida_vasp.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    html_theme = 'default'
    from aiida.manage import configuration
    configuration.IN_RT_DOC_MODE = True
    configuration.BACKEND = 'django'
else:
    import sphinx_rtd_theme  # pylint: disable=import-error
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# 0html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AiiDA-VASPdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AiiDA-VASP.tex', 'AiiDA-VASP Documentation', 'Espen Flage-Larsen, Atsushi Togo, Martin Callsen', 'manual'),
]

# Taken from AiiDA core, to be able to get API doc on RTD, we need to
# put the apidoc here.
# See also: https://github.com/rtfd/readthedocs.org/issues/1139


def run_apidoc(_):
    """Runs sphinx-apidoc when building the documentation."""
    source_dir = os.path.abspath(os.path.dirname(__file__))
    apidoc_dir = os.path.join(source_dir, 'api')
    package_dir = os.path.join(source_dir, os.pardir, os.pardir, 'aiida_vasp')

    import subprocess  # pylint: disable=import-outside-toplevel
    cmd_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(sys.prefix, 'bin', 'sphinx-apidoc'))

    options = [
        '-o',
        apidoc_dir,
        package_dir,
        '--private',
        '--force',
        '--no-headings',
        '--module-first',
        '--no-toc',
        '--maxdepth',
        '4',
    ]

    # See https://stackoverflow.com/a/30144019
    env = os.environ.copy()
    env['SPHINX_APIDOC_OPTIONS'] = 'members,special-members,private-members,undoc-members,show-inheritance'
    subprocess.check_call([cmd_path] + options, env=env)


#def setup(app):
#if os.environ.get('RUN_APIDOC', None) != 'False':
#    app.connect('builder-inited', run_apidoc)

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'aiida-vasp', 'AiiDA-VASP Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AiiDA-VASP', 'AiiDA-VASP Documentation', author, 'AiiDA-VASP',
     'A plugin to enable usage of VASP in the AiiDA workflow engine.', 'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'aiida': ('https://aiida.readthedocs.io/projects/aiida-core/en/latest/', None)
}
