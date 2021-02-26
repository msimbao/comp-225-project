import json

# TODO: Uncomment these when ready to run only from server.py, otherwise use local import versions

# from sportsData import mlb
# from sportsData import nba
# from sportsData import nfl
# from sportsData import nhl

import mlb
import nba
import nfl
import nhl

leagues = []
mlbConferences = []
nhlConferences = []
nflConferences = []
nbaConferences = []


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def setDictionaries():
    # Function to setup dictionaries of each major league
    mlbDictionary = list(mlb.get_mlb_data().keys())
    mlbData = mlb.get_mlb_data()

    for i in mlbDictionary:
        mlbConferences.append(
            {"title": i, "image": "", "children": mlbData[i], "record": ""},
        )

    nbaDictionary = list(nba.get_nba_data().keys())
    nbaData = nba.get_nba_data()

    for i in nbaDictionary:
        nbaConferences.append(
            {"title": i, "image": "", "children": nbaData[i], "record": ""},
        )

    nflDictionary = list(nfl.get_nfl_data().keys())
    nflData = nfl.get_nfl_data()

    for i in nflDictionary:
        nflConferences.append(
            {"title": i, "image": "", "children": nflData, "record": ""},
        )

    nhlDictionary = list(nhl.get_nhl_data().keys())
    nhlData = nhl.get_nhl_data()

    for i in nhlDictionary:
        nhlConferences.append(
            {"title": i, "image": "", "children": nhlData, "record": ""},
        )


def setLeagues():
    # Function to Set Starting league photos and names
    global leagues

    mlbTitle = "Major League Baseball - MLB"
    nbaTitle = "National Basketball Association - NBA"
    nflTitle = "National Football League - NFL"
    nhlTitle = "National Hockey League - NHL"

    mlbImage = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fmlb.png?v=1614216154946"
    nbaImage = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fnba-logo-transparent.png?v=1612974800974"
    nflImage = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fnfl-1-logo-png-transparent.png?v=1612974806169"
    nhlImage = "https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fnhl-1-logo-black-and-white.png?v=1612974870788"

    leagues = [
        {"title": mlbTitle, "image": mlbImage,
            "children": mlbConferences, "record": ""},
        {"title": nbaTitle, "image": nbaImage,
            "children": nbaConferences, "record": ""},
        {"title": nflTitle, "image": nflImage,
            "children": nflConferences, "record": ""},
        {"title": nhlTitle, "image": nhlImage,
            "children": nhlConferences, "record": ""}
    ]


def outPutData():
    # Function to output League and team data
    setDictionaries()
    setLeagues()

    jprint(leagues)
    y = json.dumps(leagues)

    f = open("leagues.txt", "w")
    f.write(y)
    f.close()


outPutData()
