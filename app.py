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


OPTION_DATA = {}
OPTION_LIST = []

@app.route('/resetTeams', methods=['GET', 'POST'])
def resetTeams():
    
    global OPTION_DATA

    f = open("sportsData/teamData.json", "r")
    OPTION_DATA =  json.loads(f.read())
    OPTION_LIST = [OPTION_DATA['0'],OPTION_DATA['37'],OPTION_DATA['70'],OPTION_DATA['111']]
    f.close()

    return jsonify(OPTION_LIST)

#============================================================================

@app.route('/grabTeam', methods=['GET', 'POST'])
def grabTeam():
    if 'teamId' in request.args:
        teamId = request.args['teamId']
        # print("this is the teamId:",teamId)
        TEAM = OPTION_DATA[str(teamId)]
    return jsonify(TEAM)


@app.route('/conferences', methods=['GET', 'POST'])
def option_data():

    # TODO: Replace this json read with the working output from sportDictionaries.
    # has to be made so that OPTION_DATA is also not a global variable
    # TODO: Also we need images for the team logos. Preferably urls. Example given 
    # for the top level league logos. We can also just leave logos out. They need to be 
    # added as keys to the respective league data

    global OPTION_DATA
    global OPTION_LIST

    #============================================================================

    if 'option' in request.args:
        option = request.args['option']
        OPTION_LIST = []
        for i in OPTION_DATA[option]["children"]:
            OPTION_LIST.append(OPTION_DATA[str(i)])

    # print(OPTION_DATA)
    return jsonify(OPTION_LIST)

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