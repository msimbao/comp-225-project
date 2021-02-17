
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
from flask_cors import CORS
from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib.request, urllib.error
import random
import socket
from googleSearch import bingsearch

#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Import Our Own Modules
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

import accessAPI

#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup Flask 
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Enable CORS
CORS(app)


# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')


#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup News Item Variables 
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

# Testing Data
Test_title_1 = "Broncos release veteran cornerback A.J. Bouye after one season "
Test_description_1 = "Bouye played in a mere seven games with the Broncos in 2020 while dealing with a shoulder issue before he was suspended for the remaining four contests (plus the first two of 2021) due to a violation of the league's policy on performance-enhancing drugs. He finished with 23 tackles and six passes defensed...."
Test_image_1 = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fpexels-david-morris-2190159.jpg?v=1612938092969"

Test_title_2 = "Steph Still Making History "
Test_description_2 = "In 2015-16, Stephen Curry posted the best offensive box plus/minus in NBA history. He was so dominant that he was able to rest for the entirety of the fourth quarter in 19 of his 79 games, and the Golden State Warriors won a league-record 73 regular-season games...."
Test_image_2 = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fpexels-alexandro-david-2868705.jpg?v=1612938092593"

#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////
# Setup Flask functions and end routes
#//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

#General Test Route
# @app.route('/lol')
# def rlol():
#     return jsonify(test.lol())
  
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
        SEARCH_RESULTS = []
        
        query = request.args['newsItem']
        print(query)
        news_search = bingsearch.BingSearch(query)

        SEARCH_RESULTS = news_search.getArticleList()
    else:
        SEARCH_RESULTS = [
                            { "title" : Test_title_1 ,"description":Test_description_1, "url": "#url", "image": Test_image_1},
                            { "title" : Test_title_2 ,"description":Test_description_2, "url": "#url", "image": Test_image_2}
                        ]
    # print('Search Resuls',SEARCH_RESULTS)

    return jsonify(SEARCH_RESULTS)

if __name__ == '__main__':
    app.run()