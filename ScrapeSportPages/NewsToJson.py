import json
from datetime import date
import os
from googleSearch.bingsearch import BingSearch
import time

# NBA division lists
ECATLANTA = ["ECATLANTA",
             "Boston Celtics",
             "Brooklin Nets",
             "New York Knicks",
             "Philadelphia 76ers",
             "Toronto Raptors"]

ECCENTRAL = ["ECCENTRAL",
             "Chicago Bulls",
             "Cleveland Cavaliers",
             "Detroit Pistons",
             "Indiana Pacers",
             "Milwaukee Bucks"]

ECSOUTHEAST = ["ECSOUTHEAST",
               "Atlanta Hawks",
               "Charlotte Hornets",
               "Miami Heat",
               "Orlando Magic",
               "Washington Wizards"]

WCNORTHEAST = ["WCNORTHEAST",
               "Denver Nuggets",
               "Minnesota Timberwolves",
               "Oklahoma City Thunder",
               "Portland Trail Blazers",
               "Utah Jazz"]

WCPACIFIC = ["WCPACIFIC",
             "Golden State Warriors",
             "Los Angeles Clippers",
             "Los Angeles Lakers",
             "Phoenix Suns",
             "Sacramento Kings"]

WCSOUTHWEST = ["WCSOUTHWEST",
               "Dallas Mavericks",
               "Houston Rockets",
               "Memphis Grizzlies",
               "New Orleans Pelicans",
               "San Antonio Spurs"]

# MLB Division List
NLE = ["NLE",
       "Atlanta Braves",
       "Miami Marlins",
       "New York Mets",
       "Philadelphia Phillies",
       "Washington Nationals"]

NLC = ["NLC",
       "Chicago Cubs",
       "Cincinnati Reds",
       "Milwaukee Brewers",
       "Pittsburgh Pirates",
       "St. Louis Cardinals"]

NLW = ["NLW",
       "Arizona Diamondbacks",
       "Colorado Rockies",
       "Los Angeles Dodgers",
       "San Diego Padres",
       "San Francisco Giants"]

ALE = ["ALE",
       "Baltimore Orioles",
       "Boston Red Sox",
       "New York Yankees",
       "Tampa Bay Rays",
       "Toronto Blue Jays"]

ALC = ["ALC",
       "Chicago White Sox",
       "Cleveland Indians",
       "Detroit Tigers",
       "Kansas City Royals",
       "Minnesota Twins"]

ALW = ["ALW",
       "Houston Astros",
       "Los Angeles Angels",
       "Oakland Athletics",
       "Seattle Mariners",
       "Texas Rangers"]

# NFL Division List
AFCEAST = ["AFCEAST",
           "Buffalo Bills",
           "Miami Dolphins",
           "New England Patriots",
           "New York Jets"]

AFCNORTH = ["AFCNORTH",
            "Baltimore Ravens",
            "Cincinnati Bengals",
            "Cleveland Browns",
            "Pittsburgh Steelers"]

AFCSOUTH = ["AFCSOUTH",
            "Houston Texans",
            "Indianapolis Colts",
            "Jacksonville Jaguars",
            "Tennessee Titans"]

AFCWEST = ["AFCWEST",
           "Denver Broncos",
           "Kansas City Chiefs",
           "Oakland Raiders",
           "Los Angeles Chargers"]

NFCEAST = ["NFCEAST",
           "Dallas Cowboys",
           "New York Giants",
           "Philadelphia Eagles",
           "Washington Redskins"]

NFCNORTH = ["NFCNORTH",
            "Chicago Bears",
            "Detroit Lions",
            "Green Bay Packers",
            "Minnesota Vikings"]

NFCSOUTH = ["NFCSOUTH",
            "Atlanta Falcons",
            "Carolina Panthers",
            "New Orleans Saints",
            "Tampa Bay Buccaneers"]

NFCWEST = ["NFCWEST",
           "Arizona Cardinals",
           "Los Angeles Rams",
           "San Francisco 49ers",
           "Seattle Seahawks"]

ECATLANTIC = ["ECATLANTIC",
              "Boston Bruins",
              "Buffalo Sabres",
              "Detroit Red Wings",
              "Florida Panthers",
              "Montreal Canadiens",
              "Ottawa Senators",
              "Tampa Bay Lightning",
              'Toronto Maple Leafs']

ECMETROPOLOTAN = ["ECMETROPOLOTAN",
                  "Carolina Hurricanes",
                  "Columbus Blue Jackets",
                  "New Jersey Devils",
                  "New York Islanders",
                  "New York Rangers",
                  "Philadelphia Flyers",
                  "Pittsburgh Penguins",
                  "Washington Capitals"]

WCCENTRAL = ["WCCENTRAL",
             "Chicago Blackhawks",
             "Colorado Avalanche",
             "Dallas Stars",
             "Minnesota Wild",
             "Nashville Predators",
             "St.Louis Blues",
             "Winnipeg Jets"]

WCPACIFICNHL = ["WCPACIFIC",
                "Anaheim Ducks",
                "Arizona Coyotes",
                "Calgary Flames",
                "Edmonton Oilers",
                "Los Angeles Kings",
                "San Jose Sharks",
                "Vancouver Canucks",
                "Vegas Golden Knights"]

NL = [NLE, NLC, NLW]

AL = [ALE, ALC, ALW]

MLBQUERYLIST = ["MLB", NL, AL]

ECNBA = [ECATLANTA, ECCENTRAL, ECSOUTHEAST]

WCNBA = [WCNORTHEAST, WCPACIFIC, WCSOUTHWEST]

NBAQUERYLIST = ["NBA", ECNBA, WCNBA]

AFC = [AFCEAST, AFCNORTH, AFCSOUTH, AFCWEST]

NFC = [NFCEAST, NFCNORTH, NFCSOUTH, NFCWEST]

NFLQUERYLIST = ["NFL", AFC, NFC]

ECNHL = [ECATLANTIC, ECMETROPOLOTAN]

WCNHL = [WCPACIFICNHL, WCCENTRAL]

NHLQUERYLIST = ["NHL", ECNHL, WCNHL]


def createNewNews(query):
    """Reformats and returns BingSearch results into a dictionary form that includes article title, article url,
    article image, article description, article author.

    Parameters
    ----------
    query: str
        The search keyword for BingSearch to conduct search.

    Returns
    -------
    dict
        A dictionary containing article title, article url, article image, article description, article author.
    """
    bing_search = BingSearch(query)
    newsDataBaseForm = {}

    titles = bing_search.get_titles()
    urls = bing_search.get_urls()
    images = bing_search.get_images()
    descriptions = bing_search.get_description()
    authors = bing_search.get_author()

    for i in range(0, len(titles) - 1):
        title = titles[i]
        url = urls[i]
        image = images[i]
        description = descriptions[i]
        author = authors[i]
        newsDataBaseForm['newsItem' + str(i + 1)] = {
            'Title': title,
            'Url': url,
            'Image': image,
            'Description': description,
            'Author': author
        }

    return newsDataBaseForm


def newsToJson(newsDict, fileName, directoryName):
    """This function takes a dictionary and make it into a .json file. (I chose .json instead of .txt because .json file
    could be directly read back into dictionary which I think is easier for server.py to read in.)

    Parameters
    ----------
    newsDict: dict
        A dictionary contain info of a single news article.
    fileName: str
        A str that you wish this .json file to be called.
    directoryName: str
        A str that is the directory you wish this .json file to be stored in.
    """
    fileName = fileName.replace("/", "_")
    filename = directoryName + fileName + ".json"
    with open(filename, "w") as f:
        json.dump(newsDict, f)

    return 0


def makeDirectoryToday():
    """This function creates a folder in the top directory in the name of today's date(MM_DD_YY).
    """
    # Acquire the date of the current query
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")

    # Make current day's directory
    directoryToday = "../newsJson/" + month + "_" + day + "_" + year
    if not os.path.exists(directoryToday):
        os.makedirs(directoryToday)

    return 0


def jsonDumpNewsItems(query, league_directory="", division_directory="", optional_directory=""):
    """Reformats a search result from BingSearch and turns each news Article item into a .json file in formatted
    directories.

        Parameters
        ----------
        query: str
            Search keyword for BingSearch.
        league_directory: str, optional
            Name of the league of current search. Default is an empty string.
        division_directory: str, optional
            Name of the division of current search. Default is an empty string.
        optional_directory: str, optional
            An additional parameter in case another directory level must be created.
        """
    # Acquire the date of the current query
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")

    # Build json folder for each day's news
    # Creating new directory in newsJson folder for the day's news
    newsPath = "../newsJson/" + month + "_" + day + "_" + year + "/" + league_directory + "/" + division_directory + \
               "/" + optional_directory + "/" + query

    if not os.path.exists(newsPath):
        os.makedirs(newsPath)

    News = createNewNews(query)

    for i in range(1, len(News)):
        newsToJson(News["newsItem" + str(i)], "newsItem" + str(i), newsPath + "/")

    return 0


def buildNBANews():
    # Build NBA json folder for each day's news
    jsonDumpNewsItems("NBA", "NBA", "NBA League News")

    for divisions in ECNBA:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NBA", "EC", divisions[0])

    for divisions in WCNBA:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NBA", "WC", divisions[0])

    return 0


def buildMLBNews():
    # Build MLB json folder for each day's news
    jsonDumpNewsItems("MLB", "MLB", "MLB League News")

    for divisions in NL:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "MLB", "NL", divisions[0])

    for divisions in AL:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "MLB", "AL", divisions[0])

    return 0


def buildNFLNews():
    # Build NFL json folder for each day's news
    jsonDumpNewsItems("NFL", "NFL", "NFL League News")

    for divisions in AFC:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NFL", "AFC", divisions[0])

    for divisions in NFC:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NFL", "NFC", divisions[0])

    return 0

def buildNHLNews():
    # Build NHL json folder for each day's news
    jsonDumpNewsItems("NHL", "NHL", "NHL League News")

    for divisions in ECNHL:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NHL", "EC", divisions[0])

    for divisions in WCNHL:
        for i in range(1, len(divisions)):
            jsonDumpNewsItems(divisions[i], "NHL", "WC", divisions[0])

    return 0


def buildNews():
    makeDirectoryToday()

    buildNBANews()
    buildMLBNews()
    buildNFLNews()
    buildNHLNews()

    return 0


def jsonToDict(fileName):
    with open(fileName, "r+") as file:
        newsDict = json.load(file)
    return newsDict


if __name__ == '__main__':
    start_time = time.time()
    buildNews()
    print("--- %s seconds ---" % (time.time() - start_time))
