#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'yuan'
SITENAME = u"y119777.github.io"
SITEURL = 'https://y119777.github.io'
DISQUS_SITENAME = 'y119777'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

LOCALE = 'C'
DEFAULT_LANG = u'zh_CN'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d(%A) %H:%M')

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'hide'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# menu items
MENUITEMS = [('Home', SITEURL),
            ('About', SITEURL + '/about.html'),
			('Github', 'https://github.com/'),]

# Blogroll
# LINKS = (('GitHub', 'https://github.com/kamidox'),)

# Social widget
# SOCIAL = (('微博', 'http://weibo.com/kamidox'),)

DEFAULT_PAGINATION = 10

MD_EXTENSIONS = [
        "extra",
        "toc",
        "headerid",
        "meta",
        "sane_lists",
        "smarty",
        "wikilinks",
        "admonition",
        "nl2br",
        "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"]

#CNZZ_ANALYTICS = True

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

THEME = "themes/foundation-default-colours"
#THEME = "/home/kamidox/pelican/pelican-themes/foundation-default-colours"
#THEME = "themes/tuxlite_tbs"

# weibo auth
#STATIC_PATHS = ['extra']
#EXTRA_PATH_METADATA = {
#        'extra/CNAME': {'path': 'CNAME'},
#        'esxtra/wb_305ecb5714d4db06.txt': {'path': 'wb_305ecb5714d4db06.txt'},
#        }
