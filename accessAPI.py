import requests
import json
import urllib.request, urllib.error

api_key = '67b28becd2b54160a21d4cce7e134a10'
api_url_base = 'http://newsapi.org/v2/'


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
    response = requests.get(api_url_base+'everything?q='+ query +'&from=2021-01-09&sortBy=publishedAt&apiKey='+api_key)
    jsonString=response.json()
    # jprint(response.json())
    articles = jsonString['articles']
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

# getGeneralNews("tesla")
