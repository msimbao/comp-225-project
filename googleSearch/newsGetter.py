from GoogleNews import GoogleNews
from newspaper import Article
import newsArticle
import pandas as pd


class NewsGetter:

    def __init__(self, team):
        self.team = team
        self.news = GoogleNews()
        self.news.search(team)
        self.result = self.news.result()
        self.fullList = self.__parseData()

    def __parseData(self):
        """Reads in website data, creates a data fram of all scraped articles, and then creates a list of
        newsArticle objects"""
        df = pd.DataFrame(self.result)

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
                news_page = newsArticle.NewsArticle()
                news_page.setDate(df['date'][ind])
                news_page.setMedia(df['media'][ind])
                news_page.setTitle(article.title)
                news_page.setArticle(article.text)
                news_page.setSummary(article.summary)
                news_page.setImageList(article.imgs)
                news_page.setUrl(article.url)

                newsList.append(news_page)

        return newsList

    def getArticleInfo(self):
        return self.fullList
