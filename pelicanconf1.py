#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'yuan'
SITENAME = u'y119777.github.io'
SITEURL = 'http://y119777.github.io'
#DISQUS_SITENAME = 'y119777'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh_CN'
#DATE_FORMAT={"zh":("zh_CN","%Y-%m-%d,%a"),}#日期格式设置，可按自己喜好设定
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
#MENUITEMS
MENUITEMS = [('Home', SITEURL),
      ('About', SITEURL + 'about.html'),]
MD_EXTENSIONS = [
  "extra",
  "toc",
  "headerid",
  "meta",
  "sane_lists",
  "smarty",
  "wikilinks",
  "admonition",
  "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"]
#CNZZ_ANALYTICS = True
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
THEME = "themes/foundation-default-colours"
DEFAULT_PAGINATION = 10
#RELATIVE_URLS = False   # 禁用相对路径引用
#DELETE_OUTPUT_DIRECTORY = True		 