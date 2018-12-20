#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Oivvio Polite"
SITENAME = "Liberationtech"
# SITEURL = "https://liberationtech.net"

PATH = "content"

TIMEZONE = "Europe/Stockholm"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    #    ("Pelican", "http://getpelican.com/"),
    #    ("Python.org", "http://python.org/"),
    #    ("Jinja2", "http://jinja.pocoo.org/"),
    #    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "pelican-hss"
# devrandom monospace
# THEME = "simple"
THEME = "pelican-ghostwriter"

TAGLINE = "A proper blog"

# set custom.css url.
CUSTOM_CSS_URL = "/static/custom.css"
STATIC_PATHS = ["extra", "images"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "images/selfie.jpg": {"path": "static/selfie.jpg"},
}

USER_LOGO_URL = "/static/selfie.jpg"
