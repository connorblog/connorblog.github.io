AUTHOR = "Connor"
SITENAME = "Connor's Blog"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "/home/connor/dev/connorblog.github.io/Pelican/themes/gum/"

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.jinja2content",
    "pelican.plugins.image_process",
]

# image-process plugin

IMAGE_PROCESS = {
    "article": {
        "type": "image",
        "ops": ["scale_in 50% 50% False"],
    },
}

# jinja2content plugin
JINJA2CONTENT_TEMPLATES = ["../includes"]

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
