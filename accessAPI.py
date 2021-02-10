import requests
import json
from newsapi import NewsApiClient

api_key = '67b28becd2b54160a21d4cce7e134a10'
api_url_base = 'http://newsapi.org/v2/'

# Init
newsapi = NewsApiClient(api_key='67b28becd2b54160a21d4cce7e134a10')

def jprint(obj):
    """Function the Print the JSON response of an A =PI in a nicer formated string

    Args:
        obj (string): JSON response
    """

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def getGeneralNews(query):
    """Function to get articles from an api response

    Args:
        query (string): Article Topic

    Returns:
        list: List of articles as dictionaries
    """
    response = newsapi.get_top_headlines(q=query,
                                          category='sports',
                                          language='en',
                                          country='us')
    # jprint(response.json())
    articles = response['articles']

    return articles



def getUrls(articles):
    """Function to get the urls from articles in a JSON response

    Args:
        articles (list): List of articles

    Returns:
        list: list of urls as strings
    """
    urls = []
    for article in articles:
        urls.append(article['url'])

    return urls 

def getImageUrls(articles):
    """Function to get the Image urls from articles in a JSON response

    Args:
        articles (list): List of articles

    Returns:
        list: list of Image urls as strings
    """
    urls = []
    for article in articles:
        urls.append(article['urlToImage'])

    return urls 

def getTitles(articles):
    """Function to get the titles from articles in a JSON response

    Args:
        articles (list): List of articles

    Returns:
        list: list of titles as strings
    """
    titles = []
    for article in articles:
        titles.append(article['title'])

    return titles 

def getAuthors(articles):
    """Function to get the author from articles in a JSON response

    Args:
        articles (list): List of articles

    Returns:
        list: list of authors as strings
    """
    titles = []
    for article in articles:
        titles.append(article['author'])

    return titles 

# articles = getGeneralNews("hawks")
# titles = getTitles(articles)

# for title in titles:  
#     print(title)
