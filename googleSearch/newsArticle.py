from PIL import Image
import urllib
import requests


class NewsArticle:

    def __init__(self):
        self.__date = None
        self.__media = None
        self.__title = None
        self.__article = None
        self.__imageList = None
        self.__summary = None
        self.__url = None

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setMedia(self, media):
        self.__media = media

    def getMedia(self):
        return self.__media

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setArticle(self, article):
        self.__article = article

    def getArticle(self):
        return self.__article

    def setImageList(self, imageSet):
        self.__imageList = list(imageSet)

    def getImageList(self):
        return self.__imageList

    def setSummary(self, summary):
        self.__summary = summary

    def getSummary(self):
        return self.__summary

    def setUrl(self, url):
        self.__url = url

    def getUrl(self):
        return self.__url

    def displayPicture(self):
        """Displays largest picture, still not working yet"""
        size = 0
        image = None
        for url in self.__imageList:
            im = Image.open(requests.get(url, stream=True).raw)
            height, weight = im.size
            imgSize = height * weight

            print(url)
            print(size)
            if imgSize > size:
                image = im
        # if image:
        #     image.show()

    def __repr__(self):
        return "Date: " + str(self.__date) + \
               ", Media: " + self.__media + \
               ", Title: " + self.__title +  \
               ", Article: " + self.__article +\
                ", Summary: " + self.__summary + \
                ", URL: " + self.__url + \
                ", Images: " + str(self.__imageList)

    def __str__(self):
        return "Date: " + str(self.__date) + "\n" \
                "Media: " + self.__media + "\n" \
                "Title: " + self.__title + "\n" \
                "Article: " + self.__article + "\n" \
                "Summary: " + self.__summary + "\n" \
                "URL: " + self.__url + "\n" \
                "Images: " + str(self.__imageList) + "\n"
