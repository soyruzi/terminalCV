#!/usr/bin/env python
#===============================================================================
#
#          FILE: render.py
#
#         USAGE: ./render.py
#
#   DESCRIPTION: renders the contents of about.yml into www/index.html
#
#       OPTIONS:
#  REQUIREMENTS:
#         NOTES:
#        AUTHOR: D Hauck, C Hawley
#  ORGANIZATION:
#       CREATED:
#      REVISION:
#===============================================================================

import yaml
from sys import exit
from jinja2 import Template
from htmlmin import minify

try:
     about = yaml.load(open('about.yml', 'r').read(), Loader=yaml.FullLoader)
except IOError:
    print ("You need to provide a valid about.yml file!")
    exit(1)

if about['long_description'].endswith('\n'):
    about['long_description'] = about['long_description'][:-2]

for project in about['projects']:
    if project['description'].endswith('\n'):
        project['description'] = project['description'][:-2]

template = Template(open('index.j2').read())
open('www/index.html', 'w').write(template.render(about=about))
