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
import json
from flask import Flask, request, render_template, jsonify, Response
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
query = "Testing Query"
NEWS_ARTICLES = ["Testing Articles"]
NEWS_URLS = ["Testing Urls"]
NEWS_TITLES = ["Testing Titles - If This Works, Server is functional"]

SEARCH_RESULTS = []


#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup Flask functions and end routes
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////




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
        query = ""
        NEWS_ARTICLES = []
        NEWS_URLS = []
        NEWS_IMAGE_URLS = []
        NEWS_TITLES = []
        NEWS_AUTHORS = []
        SEARCH_RESULTS = []
        
        query = request.args['newsItem']
        NEWS_ARTICLES =accessAPI.getGeneralNews(query)
        NEWS_URLS =accessAPI.getUrls(NEWS_ARTICLES)
        NEWS_IMAGE_URLS =accessAPI.getImageUrls(NEWS_ARTICLES)
        NEWS_TITLES=accessAPI.getTitles(NEWS_ARTICLES)
        NEWS_AUTHORS=accessAPI.getAuthors(NEWS_ARTICLES)
        # NEWS_TITLES.append(request.args['newsItem'])
        for i in range(len(NEWS_ARTICLES)):
          SEARCH_RESULTS.append( { "title" : NEWS_TITLES[i], "url": NEWS_URLS[i], "image": NEWS_IMAGE_URLS[i],"authors": NEWS_AUTHORS[i]} )
    else:

      SEARCH_RESULTS = [{ "title" : "Title Of an Article", "url": "#url", "image": "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Ffootball_05.jpeg?v=1612922073108","authors": "Author of Article"}]
 
#     # Return the list of remembered News. 
#     return Response(json.dumps(js),  mimetype='application/json')
    print('Search Resuls',SEARCH_RESULTS)
    # print('News Title',NEWS_TITLES)
    # Return the list of remembered News. 
    # return Response(json.dumps(SEARCH_RESULTS),  mimetype='application/json')
    return jsonify(SEARCH_RESULTS)

  
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Run Server
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

if __name__ == '__main__':
    app.run()