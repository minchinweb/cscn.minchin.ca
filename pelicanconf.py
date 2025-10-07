#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

from minchin.pelican.plugins import autoloader
# from pelican.plugins import seafoam

# Caching
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

AUTHOR = "William Minchin"
SITENAME = "Minchin.ca"
# SITEURL = 'http://cscn.minchin.ca'
SITEURL = ""
SITE_ROOT_URL = "http://minchin.ca"

TIMEZONE = "America/Edmonton"

DEFAULT_LANG = "en"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# static paths will be copied under the same name
STATIC_PATHS = [
    "images",
    "../extras",
    "css",
    "projects/design",
    "../.gitattributes",
    "../.gitignore",
    "../README.txt",
]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    "../.gitattributes": {"path": ".gitattributes"},
    "../.gitignore": {"path": ".gitignore"},
    "../README.txt": {"path": "README.txt"},
    "../extras/minchin.ico": {"path": "favicon.ico"},
}

# Custom settings
# FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')  #default?
MARKUP = (
    "rst",
    "md",
    "markdown",
    "mkd",
    "mdown",
)  # don't include htm and html files
READERS = {"html": None, "htm": None}
PATH = "content"
# OUTPUT_PATH = '../minchinweb.github.io-temp/'  # default is 'output/'

# Add Blog to sidebar
# MENUITEMS = (
#     ("Blog", "http://blog.minchin.ca/", "fa fa-pencil"),
#     ("Genealogy", "https://genealogy.minchin.ca/", "glyphicon glyphicon-tree-deciduous"),
# )
# DISPLAY_PAGES_ON_MENU = True

# disable Tags, etc
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_URL = ""
CATEGORIES_SAVE_AS = ""
ARTICLE_URL = ""
ARTICLE_SAVE_AS = ""
AUTHORS_URL = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_URL = ""
ARCHIVES_SAVE_AS = ""
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TEMPLATE_PAGES = {
    "404.html": "404.html",
}

# Theme Related
TYPOGRIFY = True
# THEME = seafoam.get_path()
BOOTSTRAP_THEME = "seafoam"
SITELOGO = "images/MinchindotCA-200.png"
SITELOGO_SIZE = "100%"
# PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = "favicon.ico"
USE_OPEN_GRAPH = True
# CUSTOM_CSS = 'css/minchin-ca.css'  # folded into Bootstrap theme
DOCUTIL_CSS = False
INDEX_COPY_DATE = "2007-{}".format(str(date.today().year)[-2:])
NAVBAR_ON_TOP = True
DISPLAY_ARCHIVES_ON_MENU = False

# Plugins
# PLUGIN_PATHS = [
#     "../pelican-plugins",
# ]
PLUGINS = [
    # "minchin.pelican.jinja_filters",  # required by seafoam theme
    "minchin.pelican.plugins.autoloader",
]
AUTOLOADER_NAMESPACES = autoloader.DEFAULT_NAMESPACE_LIST + [
    "pelican.plugins",
    # other namespaces
]

ASSET_CSS = False
ASSET_JS = False

SITEMAP = {
    "format": "xml",
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.def_list": {},
    },
    "output_format": "html5",
}

# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` might be useful...


# # Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False

IMAGE_PROCESS = {
    # set for 12 col width
    "article-feature": ["scale_in 1140 1140 False"],
    "9-col": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "srcset": [
                    (
                        "768w",
                        ["scale_in 750 562.5 True"],
                    ),  # actually 12 cols (full width) on smallest screens
                    ("992w", ["scale_in 727.5 545.5 True"]),
                    ("1200w", ["scale_in 877.5 658 True"]),
                ],
                "sizes": "100vw",
            },
        ],
        "default": ("default", "1200w"),
    },
    "index-thumbnail": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "srcset": [
                    (
                        "768w",
                        ["scale_in 187.5 140.5 True"],
                    ),  # actually 12 cols (full width) on smallest screens
                    # 157.5
                    ("992w", ["scale_in 212.5 182 True"]),
                    ("1200w", ["scale_in 262.5 219.5 True"]),
                ],
                "sizes": "100vw",
            },
        ],
        "default": ("default", "1200w"),
    },
}
IMAGE_PROCESS_PARSER = SEAFOAM_PARSER = "html5lib"

# Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False
