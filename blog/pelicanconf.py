#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Oivvio Polite"
SITENAME = "Liberationtech"
SITEURL = "https://liberationtech.net"

ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}/index.html"

PATH = "content"

TIMEZONE = "Europe/Stockholm"
LOCALE = ("en_US.UTF-8",)

DEFAULT_LANG = "en"

MENU_GITHUB = "https://github.com/oivvio"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#    ("Pelican", "http://getpelican.com/"),
#    #    ("Python.org", "http://python.org/"),
#    #    ("Jinja2", "http://jinja.pocoo.org/"),
#    #    ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "pelican-hss"
# devrandom monospace
# THEME = "simple"
#
#
# THEME = "pelican-ghostwriter"

HOME_COLOR = "black"

# HOME_COVER = "https://casper.ghost.org/v1.0.0/images/welcome.jpg"

STATIC_PATHS = ["extra", "images", "videoposters"]

# installed in venv with `pelican-themes`
THEME = "attila"
CSS_OVERRIDE = ["extra/custom.css"]


TAGLINE = "A proper blog"

PLUGINS = ["jinja2content"]

IGNORE_FILES = ["snippets"]
JINJA2CONTENT_TEMPLATES = ["snippets"]

# EXTRA_PATH_METADATA = {
#    "extra/custom.css": {"path": "static/custom.css"},
#    "images/selfie.jpg": {"path": "static/selfie.jpg"},
# }

# USER_LOGO_URL = "/static/selfie.jpg"
