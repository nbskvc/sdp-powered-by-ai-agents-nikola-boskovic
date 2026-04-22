"""Sphinx configuration file for Kata documentation."""

# -- Project information -----------------------------------------------------
project = "Game of Life"
copyright = "2026, Nikola Boskovic"
author = "Nikola Boskovic"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_wagtail_theme",
    "myst_parser",
    "sphinx_new_tab_link",
]

new_tab_link_show_external_link_icon = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_wagtail_theme"

html_theme_options = {
    "project_name": "Game of Life",
    "github_url": "https://github.com/nbskvc/sdp-powered-by-ai-agents-nikola-boskovic",
    "footer_links": "",
}

html_show_copyright = True
html_last_updated_fmt = "%b %d, %Y"
html_show_sphinx = False

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]
