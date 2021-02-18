from bingsearch import BingSearch


query = "pittsburgh pirates"
search = BingSearch(query)
list = search.getArticleList()

# for i in list:
#     article = Article(i["url"])
#     try:
#         article.download()
#         article.parse()
#         article.nlp()
#
#     except:
#         pass
#
#     print(article.authors)

print(list)