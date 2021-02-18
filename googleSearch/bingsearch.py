import json
import requests


class BingSearch:
    def __init__(self, query):
        __articleList = self.__setUp(query)
        self.__filteredList = self.__filterArticles(__articleList)

    def __setUp(self, query):
        subscription_key = "a18adff624cb4da7a6c9c52a2fc2f28a"
        search_term = query
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        list = json.loads(search_results)
        return list["value"]

    def __filterArticles(self, articleList):
        list = []
        for i in articleList:
            newDict = {}
            try:
                newDict["title"] = i["name"]
                newDict["url"] = i["url"]
                newDict["image"] = i["image"]["thumbnail"]["contentUrl"]
                newDict["description"] = i["description"]
                newDict["author"] = i["provider"][0]["name"]
                list.append(newDict)
            except:
                pass

        return list

    def getArticleList(self):
        return self.__filteredList

    def __getObject(self, object):
        list = []
        for i in self.__filteredList:
            list.append(i[object])
        return list

    def getTitles(self):
        return self.__getObject("title")

    def getUrls(self):
        return self.__getObject("url")

    def getImages(self):
        return self.__getObject("image")

    def getDescription(self):
        return self.__getObject("description")

    def getAuthor(self):
        return self.__getObject("author")


if __name__ == '__main__':
    search = "Pittsburgh Penguins"
    bing_search = BingSearch(search)
    list = bing_search.getArticleList()
    print(bing_search.getAuthor())

