import pyrebase
from NewsToJson import *

CONFIG = {
    "apiKey": "AIzaSyDM0YYvGQFSc9qy6jh2hpxZy_87B8eNc3o",
    "authDomain": "webapp-43db3.firebaseapp.com",
    "databaseURL": "https://webapp-43db3-default-rtdb.firebaseio.com",
    "projectId": "webapp-43db3",
    "storageBucket": "webapp-43db3.appspot.com",
    "messagingSenderId": "967819702334",
    "appId": "1:967819702334:web:2ce0a6c7293ac51b3a616f",
    "measurementId": "G-DP1Q3X9X1K"
}

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
       "St Louis Cardinals"]

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
             "St Louis Blues",
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


def _get_path(team):
    # NBA
    if team in ECCENTRAL:
        return "NBA", "EC", "ECCENTRAL"
    elif team in ECSOUTHEAST:
        return "NBA", "EC", "ECSOUTHEAST"
    elif team in ECATLANTA:
        return "NBA", "EC", "ECATLANTA"
    elif team in WCSOUTHWEST:
        return "NBA", "WC", "WCSOUTHWEST"
    elif team in WCPACIFIC:
        return "NBA", "WC", "WCPACIFIC"
    elif team in WCNORTHEAST:
        return "NBA", "WC", "WCNORTHEAST"
    # MLB
    elif team in NLW:
        return "MLB", "NL", "NLW"
    elif team in NLE:
        return "MLB", "NL", "NLE"
    elif team in NLC:
        return "MLB", "NL", "NLC"
    elif team in ALW:
        return "MLB", "AL", "ALW"
    elif team in ALE:
        return "MLB", "AL", "ALE"
    elif team in ALC:
        return "MLB", "AL", "ALC"
    # NFL
    elif team in NFCWEST:
        return "NFL", "NFC", "NFCWEST"
    elif team in NFCEAST:
        return "NFL", "NFC", "NFCEAST"
    elif team in NFCNORTH:
        return "NFL", "NFC", "NFCNORTH"
    elif team in NFCSOUTH:
        return "NFL", "NFC", "NFCSOUTH"
    elif team in AFCWEST:
        return "NFL", "AFC", "AFCWEST"
    elif team in AFCEAST:
        return "NFL", "AFC", "AFCEAST"
    elif team in AFCNORTH:
        return "NFL", "AFC", "AFCNORTH"
    elif team in AFCSOUTH:
        return "NFL", "AFC", "AFCSOUTH"
    # NHL
    elif team in ECATLANTIC:
        return "NHL", "EC", "ECATLANTIC"
    elif team in ECMETROPOLOTAN:
        return "NHL", "EC", "ECMETROPOLOTAN"
    elif team in WCPACIFICNHL:
        return "NHL", "WC", "WCPACIFIC"
    elif team in WCCENTRAL:
        return "NHL", "WC", "WCCENTRAL"


def _get_file_name():
    with open("/Users/declanelias/PycharmProjects/comp-225-project/firebasefile.txt") as f:
        for line in f:
            pass
        return line


def get_news_from_firebase(team):
    firebase = pyrebase.initialize_app(CONFIG)
    db = firebase.database()
    file = _get_file_name()
    league, conference, division = _get_path(team)
    dict = (db.child(file).child(league).child(conference).child(division).child(team).get().val())
    return list(dict.values())
