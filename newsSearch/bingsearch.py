import json
import requests
import html
from newsSearch.logoDictionary import logo_dict


class BingSearch:
    def __init__(self, query):
        """
        Initializes the BingSearch object with a query. It passes the query to self.__get_from_bing
        which returns a list of dictionaries containing data of articles about the search. It then filters
        the list by passing it to self.__filtered_articles. It also initializes the team logo dictionary
        which contains a link to the image of each team's logo.
        """
        __articleList = self.__get_from_bing(query)
        self.team_logo_dict = logo_dict
        self.__filteredList = self.__filter_articles(__articleList, query)

    def __get_from_bing(self, query):
        """
        Given the query, uses the API key from Bing News API to search for news articles.
        It then converts the JSON object returned by the API into a list of dictionaries
        containing data about the article. And returns that list
        """
        subscription_key = "728de062afa9454da647014659c84b22"
        search_term = query
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term,
                  "count": 10,
                  "textFormat": "HTML",
                  "mkt": "en-US"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        return json.loads(search_results)["value"]

    def __filter_articles(self, article_list, query):
        """
        Takes the list returned by self.__get_from_bing() and creates a list of new dictionaries
        containing the data necessary for what we need. It also tries to get an image from the
        list returned by the Bing Search, but if there is not article, it uses the query to
        get the team logo from the team logo dictionary. It then returns a the list of dictionaries
        sorted by date of the article.
        """
        list = []
        news_id = 0
        for i in article_list:
            new_dict = {"title": html.unescape(i["name"]),
                        "url": i["url"],
                        "description": html.unescape(i["description"]),
                        "author": html.unescape(i["provider"][0]["name"]),
                        "id": news_id,
                        "date published": i["datePublished"]}

            news_id += 1
            try:
                new_dict["image"] = i["image"]["thumbnail"]["contentUrl"] + "&h=500&p=0"
            except KeyError:
                try:
                    new_dict["image"] = self.team_logo_dict[query]
                except:
                    new_dict["image"] = None
            list.append(new_dict)

        return sorted(list, key=lambda k: k["date published"], reverse=True)

    def get_article_list(self, n=20):
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

    def get_ids(self):
        return self.__get_object("id")

    def get_date(self):
        return self.__get_object("date published")


if __name__ == '__main__':
    search = "Tampa Bay Lightning"
    bing_search = BingSearch(search)
    a = bing_search.get_article_list()
    for i in a:
        print(i)
