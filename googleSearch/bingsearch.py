import json
import requests
import html
import re


class BingSearch:
    def __init__(self, query):
        __articleList = self.__set_up(query)
        self.__filteredList = self.__filter_articles(__articleList)

    def __set_up(self, query):
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

    def __filter_articles(self, articleList):
        list = []
        for i in articleList:
            newDict = {}
            try:

                newDict["title"] = self.__clean_title(i["name"])
                newDict["url"] = i["url"]
                newDict["image"] = i["image"]["thumbnail"]["contentUrl"]
                newDict["description"] = i["description"]
                newDict["author"] = i["provider"][0]["name"]
                list.append(newDict)
            except:
                pass

        return list

    def __clean_title(self, title):
        title = self.__clean_html(title)
        title = self.__clean_xml(title)
        return title

    def __clean_html(self, string):
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', string)
        return clean_text

    def __clean_xml(self, string):
        return html.unescape(string)

    def get_article_list(self):
        return self.__filteredList

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
    search = "Pittsburgh Steelers"
    bing_search = BingSearch(search)
    articles = bing_search.get_titles()
    print(articles)
