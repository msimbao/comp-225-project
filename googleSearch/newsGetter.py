from GoogleNews import GoogleNews
from newspaper import Article
import newsArticle
import pandas as pd


def initialize(query):
    news = GoogleNews()
    news.search(query)
    return news.result()

def parseData(query):
    """Reads in website data, creates a data fram of all scraped articles, and then creates a list of
    newsArticle objects"""

    result = initialize(query)
    df = pd.DataFrame(result)
    return createDict(df)

def createDict(df):
    newsList = []
    for ind in df.index:
        article = Article(df['link'][ind])
        try:
            article.download()
            article.parse()
            article.nlp()

        except:
            pass

        if article.text:
            dict = {}
            dict["title"] = article.title
            dict["url"] = article.url
            dict["image"] = df['images']
            #  = newsArticle.NewsArticle()
            # news_page.setDate(df['date'][ind])
            # news_page.setMedia(df['media'][ind])
            # news_page.setTitle(article.title)
            # news_page.setArticle(article.text)
            # news_page.setSummary(article.summary)
            # news_page.setImageList(article.imgs)
            # news_page.setUrl(article.url)
            #
            # newsList.append(news_page)

    return newsList