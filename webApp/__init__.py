# coding=UTF-8
# -*- coding: UTF-8 -*-
import os

import cherrypy
from cherrypy.lib.static import serve_file

from jinja2 import Template, Environment, FileSystemLoader

#class level variables
localDir=os.path.dirname(__file__)
absDir=os.path.join(os.getcwd(), localDir)
current_dir=os.path.dirname(os.path.abspath(__file__))

#setup some rendering templates
env=Environment(loader=FileSystemLoader(current_dir), trim_blocks=True)

class Root:

    @cherrypy.expose
    def index(self):
        template_index=env.get_template('index.html')
        return template_index.render()