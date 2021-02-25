"""
Gets NBA team data by scraping basketball-reference.com
standings

@Title: nba.py
@Author: Ty, Declan, Jack, Mphatso

"""



from scraper import *


def _set_nba_data(url):
    tables = get_tables(url)
    list = []
    for i in tables:
        for idx in range(len(i) - 1):
            team_dict = {"title": i[0][idx + 1],
                         "record": i[1][idx + 1] + "-" + i[2][idx + 1],
                         "image":"",
                         "children":""}
            list.append(team_dict)

    dict = {"Eastern Conference": list[0:15],
            "Western Conference": list[15:30]}
    return dict


def get_nba_data(year=2021):
    url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)
    return _set_nba_data(url)


print(get_nba_data()["Eastern Conference"])
