import newsGetter
from GoogleNews import GoogleNews
from PIL import Image
import base64
from newspaper import Article
import pandas as pd
from bingsearch import BingSearch
from newspaper import article


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

print(len(list))