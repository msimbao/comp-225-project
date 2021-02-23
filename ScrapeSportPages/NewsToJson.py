from googleSearch import bingsearch
import json
from datetime import date
import os

from googleSearch.bingsearch import BingSearch

def createNewNews(query):
    bing_search = BingSearch(query)
    newsDataBaseForm = {}

    titles = bing_search.get_titles()
    urls = bing_search.get_urls()
    images = bing_search.get_images()
    descriptions = bing_search.get_description()
    authors = bing_search.get_author()

    for i in range(0, len(titles) - 1):
        title = titles[i]
        url = urls[i]
        image = images[i]
        description = descriptions[i]
        author = authors[i]
        newsDataBaseForm['newsItem' + str(i + 1)] = {
                'Title': title,
                'Url': url,
                'Image': image,
                'Description': description,
                'Author': author
                }

    return newsDataBaseForm

def newsToJson(newsDict, fileName, directoryName):
    fileName = fileName.replace("/", "_")
    filename = directoryName + fileName + ".json"
    with open(filename, "w") as f:
        json.dump(newsDict, f)

    return 0

def buildLeagueNews():
    # Acquire the date of the current query
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")

    # Make current day's directory
    directoryToday = month + "_" + day + "_" + year
    if not os.path.exists(directoryToday):
        os.makedirs(directoryToday)

    # Build NBA json folder for each day's news
    # Creating new directory in newsJson folder for the day's news
    newsNBAPath = "../newsJson/" + month + "_" + day + "_" + year + "/NBANews" + month + "_" + day + "_" + year

    if not os.path.exists(newsNBAPath):
        os.makedirs(newsNBAPath)

    NBANews = createNewNews("NBA")

    for i in range(1, len(NBANews)):
        newsToJson(NBANews["newsItem" + str(i)], "newsItem" + str(i), newsNBAPath + "/")

    # Build MLB json folder for each day's news
    # Creating new directory in newsJson folder for the day's news
    newsMLBPath = "../newsJson/" + month + "_" + day + "_" + year + "/MLBNews" + month + "_" + day + "_" + year

    if not os.path.exists(newsMLBPath):
        os.makedirs(newsMLBPath)

    MLBNews = createNewNews("MLB")

    for i in range(1, len(MLBNews)):
        newsToJson(MLBNews["newsItem" + str(i)], "newsItem" + str(i), newsMLBPath + "/")

        # Build MLB json folder for each day's news
        # Creating new directory in newsJson folder for the day's news
    newsNFLPath = "../newsJson/" + month + "_" + day + "_" + year + "/NFLNews" + month + "_" + day + "_" + year

    if not os.path.exists(newsNFLPath):
        os.makedirs(newsNFLPath)

    NFLNews = createNewNews("NFL")

    for i in range(1, len(NFLNews)):
        newsToJson(NFLNews["newsItem" + str(i)], "newsItem" + str(i), newsNFLPath + "/")

    return 0


def jsonToDict(fileName):
    with open(fileName, "r+") as file:
        newsDict = json.load(file)
    return newsDict

if __name__ == '__main__':
    buildLeagueNews()
