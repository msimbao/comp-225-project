#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main Server File for running the flask app.

@Title: server.py
@Author: Ty, Declan, Jack, Mphatso
"""

#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Import Third Party Modules
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

import os
from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib.request, urllib.error
import random
import socket

#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Import Our Own Modules
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

import test
import accessAPI


#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup Flask 
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')


#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup News Item Variables 
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

# News database. Store news in memory for now. 
query = "testing"
NEWS_ARTICLES = []
NEWS_URLS = []
NEWS_TITLES = []


#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup Flask functions and end routes
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

@app.after_request
def apply_kr_hello(response):
    """Adds some headers to all responses."""
  
    # Made by Kenneth Reitz. 
    if 'MADE_BY' in os.environ:
        response.headers["X-Was-Here"] = os.environ.get('MADE_BY')
    
    # Powered by Flask. 
    response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
    return response


@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

@app.route('/lol')
def rlol():
    return jsonify(test.lol())
  
@app.route('/news', methods=['GET', 'POST'])
def news():
    """Simple API endpoint for news. 
     Transient and Only Exists as long as the server is running
     For this case, we wont be storing data here but could build our
     user authentication systems using firebase
    """
  
    # Add a news item to the in-memory database, if given. 
    if 'newsItem' in request.args:
        query = request.args['newsItem']
        NEWS_ARTICLES = accessAPI.getGeneralNews(query)
        NEWS_URLS = accessAPI.getUrls(NEWS_ARTICLES)
        NEWS_TITLES = accessAPI.getTitles(NEWS_ARTICLES)
        # NEWS_TITLES.append(request.args['newsItem'])
    
    # Return the list of remembered News. 
    return jsonify(NEWS_TITLES)

if __name__ == '__main__':
    app.run()