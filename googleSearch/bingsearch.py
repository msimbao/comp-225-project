import json
import requests
import html
import re


class BingSearch:
    def __init__(self, query):
        __articleList = self.__set_up(query)
        self.__filteredList = self.__filter_articles(__articleList, query)

    def __set_up(self, query):
        list1 = self.__get_from_bing(query, 0)
        list2 = self.__get_from_bing(query, 100)
        return list1["value"] + list2["value"]

    def __get_from_bing(self, query, offset):
        subscription_key = "a18adff624cb4da7a6c9c52a2fc2f28a"
        search_term = query
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term,
                  "count": 100,
                  "offset": offset,
                  "textFormat": "HTML",
                  "mkt": "en-US"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        return json.loads(search_results)

    def __filter_articles(self, articleList, query):
        list = []
        # print(len(articleList))
        for i in articleList:
            newDict = {}

            newDict["title"] = html.unescape(i["name"])
            newDict["url"] = i["url"]
            newDict["description"] = html.unescape(i["description"])
            newDict["author"] = i["provider"][0]["name"]
            try:
                newDict["image"] = i["image"]["thumbnail"]["contentUrl"] + "&h=500&p=0"
            except KeyError:
                newDict["image"] = None
            list.append(newDict)

        return list

    # def __get_team_logo(self, team_name):
    #     team_name = team_name.replace(" ", "+")
    #     url = "https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t={}".format(team_name)
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     search_results = json.dumps(response.json(), indent=4)
    #     return json.loads(search_results)["teams"][0]['strTeamBadge']

    def get_article_list(self, n=50):
        if n > len(self.__filteredList):
            return self.__filteredList
        else:
            return self.__filteredList[0:n]

    def __get_object(self, object):
        list = []
        for i in self.__filteredList:
            list.append(i[object])
        return list

    def get_titles(self):
        return self.__get_object("title")

    def get_urls(self):
        return self.__get_object("url")

    def get_images(self):
        return self.__get_object("image")

    def get_description(self):
        return self.__get_object("description")

    def get_author(self):
        return self.__get_object("author")


if __name__ == '__main__':
    search = "Pittsburgh Pirates"
    bing_search = BingSearch(search)
    articles = bing_search.get_article_list()
    print(articles)
    print(len(articles))
