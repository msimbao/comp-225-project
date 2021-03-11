#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Server File for running the flask app.

@Title: server.py
@Author: Ty, Declan, Jack, Mphatso

"""

# Import Third Party Modules

import os
import json
from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS
import urllib.request, urllib.error

# Import Our Own Modules

# TODO: Make sportDictionaries and other packages get imported to server.py. Essentially, the others are
# working but scraper seems to refuse to work. I've set all of them up in sportDictionaries.py
# to get the data the way we need it for vue so we just need a way to make the leagues output from
# sportDictionaries get imported to here. Below i was testing individual modules

from googleSearch import bingsearch
# from sportsData import sportDictionaries

# Setup Flask 
# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Enable CORS
CORS(app)

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Setup Flask functions and end routes

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('intro.html')

@app.route('/home')
def appPage():
    """Displays the Intro Page"""
    return render_template('index.html')

@app.route('/setTeamsJson', methods=['GET', 'POST'])
def setTeamsJson():
    """[summary]
    Simple endpoint to fetch the teams.json file and read and jsonify it to be used in javascript

    Returns: OPTION_DATA the teams.json file jsonified to a javascript object
    """
    OPTION_DATA = {}

    f = open("sportsData/teamData.json", "r")
    OPTION_DATA =  json.loads(f.read())
    f.close()

    return jsonify(OPTION_DATA)


@app.route('/news', methods=['GET', 'POST'])
def news():
    """Simple API endpoint for news. 
     Transient and Only Exists as long as the server is running
     For this case, we wont be storing data here but could build our
     user authentication systems using firebase
    """
    SEARCH_RESULTS = []

    # Add a news item to the in-memory database, if given. 
    if 'newsItem' in request.args:
        query = ""
        SEARCH_RESULTS = []
        
        query = request.args['newsItem']
        number = request.args['number']
        logo = request.args['logo']
        print(query)
        news_search = bingsearch.BingSearch(query)

        SEARCH_RESULTS = news_search.get_article_list(n=int(number))
    # else:
    #     SEARCH_RESULTS = []
    # print('Search Resuls',SEARCH_RESULTS)
    # print(SEARCH_RESULTS)

    return jsonify( {'news':SEARCH_RESULTS,'logoUrl':logo} )


if __name__ == '__main__':
    app.run()