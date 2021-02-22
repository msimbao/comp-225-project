from googleSearch import bingsearch
import json
import pickle
from datetime import date
import schedule
import time
import os

filename = "/foo/bar/baz.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("FOOBAR")

def getNews(query):
    bing_search = BingSearch(query)
    return bing_search

def createNewNews(search):
    newsDataBaseForm = {}

    for i in length(search):
        newsDict = search[i - 1]
        title = newsDict["title"]
        url = newsDict["url"]
        image = newsDict["image"]
        description= newsDict["description"]
        author = newsDict["author"]
        newsDataBaseForm['newsItem' + str(i)] = {
                'Title': title,
                'Url': url,
                'Image': image,
                'Description': description,
                'Author': author
             }

        return newsDataBaseForm

def newsToJson(newsDict, fileName):
    filename = "../newsJson/" + fileName + ".json"
    # print(filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # print(filename)
    with open(filename, "w") as f:
        json.dump(newsDict, f)

def buildLeagueNews():
    today = date.today()

    # dd/mm/YY
    d = today.strftime("%m/%d/%Y")

    NBANews = createNewNews(getNews("NBA"))
    newsToJson(NBANews, "NBANews" + d)

    MLBNews = createNewNews(getNews("MLB"))
    newsToJson(MLBNews, "MLBNews" + d)

    NFLNews = createNewNews(getNews("NFL"))
    newsToJson(NFLNews, "NFLNews" + d)


def jsonToDict(fileName):
    with open(fileName, "r+") as file:
        newsDict = json.load(file)
    return newsDict

if __name__ == '__main__':
    buildLeagueNews()


    # L = {}
    # L["lol"] = "nb"
    # L["nb"] = "bbb"
    # newsToJson(L, "Lalala")
    # with open("sample.json", "w") as outfile:
    #     json.dump(L, outfile)
    # with open("sample.json", "r+") as outfile:
    #     L_new = json.load(outfile)
    # print(L_new)

# import firebase
# firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
# result = firebase.get('/users', None)
# print (result)
# {'1': 'John Doe', '2': 'Jane Doe'}