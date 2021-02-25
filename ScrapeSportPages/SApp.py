import pyrebase
import os
import time
from datetime import date
import json

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


def upLoadNewsJsonToFireBaseStorage():
    """
    This method should be run on the server for daily/ half day basis so that local json files that each stores info
    about a sports news website could be uploaded to the firebase storage. Run the buildLeagueNews() function in
    NewsToJson.py before running this method.
    """
    # Initialize firebase
    firebase = pyrebase.initialize_app(CONFIG)
    storage = firebase.storage()

    paths_local = exploreNewsJson()
    paths_on_cloud = []

    for directory in paths_local:
        paths_on_cloud.append(directory.replace("../newsJson", "newsJson"))

    start_time = time.time()

    for i in range(0, len(paths_local)):
        storage.child(paths_on_cloud[i]).put(paths_local[i])

    print(time.time() - start_time)

    return 0


def downLoadNewsJsonToLocal():
    """
    This method downloads all .json files of current day to local(server) storage.
    """
    # Initialize firebase
    firebase = pyrebase.initialize_app(CONFIG)
    storage = firebase.storage()

    # Acquire the date of the current query
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")

    newsListTodayDirectoryOnCloud = "newsJson" + "/" + month + "_" + day + "_" + year + "/" + "directoryList.json"
    newsListTodayDirectoryLocal = "../newsJson" + "/" + month + "_" + day + "_" + year + "/" + "directoryList.json"

    if not os.path.exists("../newsJson" + "/" + month + "_" + day + "_" + year):
        os.makedirs("../newsJson" + "/" + month + "_" + day + "_" + year)

    storage.child(newsListTodayDirectoryOnCloud).download(
        newsListTodayDirectoryLocal)

    newsListTodayDirectories = jsonToArray("../newsJson" + "/" + month + "_" + day + "_" + year + "/" + \
                                           "directoryList.json")

    for eachDirectory in newsListTodayDirectories:
        path_on_cloud = eachDirectory.replace("../", "")
        if not os.path.exists(eachDirectory):
            os.makedirs(eachDirectory)
        storage.child(path_on_cloud).download(eachDirectory)
        
    return 0


def exploreNewsJson():
    directory = "../newsJson"

    # Acquire the date of the current query
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")

    newsJsonList = []

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            directory = os.path.join(subdir, file)
            newsJsonList.append(directory.replace("\\", "/"))

    directoryListName = directory + "/" + month + "_" + day + "_" + year + "/" + "directoryList"

    with open(directoryListName, "w") as f:
        json.dump(newsJsonList, f)

    newsJsonList.append(directoryListName.replace("\\", "/"))

    return newsJsonList


def jsonToArray(fileName):
    with open(fileName, "r+") as file:
        directories = json.load(file)
    return directories


if __name__ == '__main__':
    # TODO: Install package pyrebase using command pip install pyrebase. P.S.: If error occurred during installation,
    #  try pip install --upgrade setuptools, it might need you to download Visual C++ 14 from the link given first.
    firebase = pyrebase.initialize_app(CONFIG)
    storage = firebase.storage()
    storage.child("images/test.jpg").put("../image/paper_mockups/1.jpg")
    # TODO: Go to firebase project, open console, go to Storage under Build. Check in the file tab if test.jpg exists
    #  in the directory images. If this works, uncomment the call below and run it. P.S.: It took me around 10 min to
    #  create all the .json files, so it might a while to upload to firebase.
    # upLoadNewsJsonToFireBaseStorage()
