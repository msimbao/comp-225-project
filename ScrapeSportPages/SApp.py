import pyrebase
from pathlib import Path

config = {
    "apiKey": "AIzaSyDM0YYvGQFSc9qy6jh2hpxZy_87B8eNc3o",
    "authDomain": "webapp-43db3.firebaseapp.com",
    "databaseURL": "https://webapp-43db3-default-rtdb.firebaseio.com",
    "projectId": "webapp-43db3",
    "storageBucket": "webapp-43db3.appspot.com",
    "messagingSenderId": "967819702334",
    "appId": "1:967819702334:web:2ce0a6c7293ac51b3a616f",
    "measurementId": "G-DP1Q3X9X1K"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

"""
This method should be run on the server for daily/ half day basis so that local json files that each stores info about a
sports news website could be uploaded to the firebase storage. Run the buildLeagueNews() function in StoreWebToFireBase.py before r-
unning this method.
"""

# TODO: Make more directories for different categories and teams.

def upLoadNewJsonToFireBaseStorage():

    path_on_cloud = "newsJson"
    path_local = "../newsJson"
    directory = os.fsencode(path_local)
    filenames = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filenames.append(filename)
        storage.child(path_on_cloud + filename).put(path_local + filename)

    fileName = "jsonFileNames.json"
    os.makedirs(os.path.dirname(path_local + fileName), exist_ok = True)
    with open(path_local + fileName, "w") as f:
        json.dump(filenames, f)

    storage.child(path_on_cloud + fileName).put(path_local + fileName)

    return 0