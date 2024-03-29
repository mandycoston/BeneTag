import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import entities

"""
Creates a form to search for a Product
"""
class CreateProductSearchPage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'searchproduct.html')
        self.response.out.write(template.render(path, template_values))

"""
Page that stores Factory in datastore
"""
class SearchResultPage(webapp.RequestHandler):
    def post(self):
        query = self.request.get('query')
        productlist = entities.Product.all()

        matches = [p for p in productlist if query.lower() in p.name.lower()]
        template_values = {
            'matches': matches
        }
        path = os.path.join(os.path.dirname(__file__), 'searchresult.html')
        self.response.out.write(template.render(path, template_values))
