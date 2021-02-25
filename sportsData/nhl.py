"""
Gets NHL team data by scraping hockey-reference.com
standings

NOTE: only works for 2021 season due to restructuring
of conferences

@Title: nhl.py
@Author: Ty, Declan, Jack, Mphatso

"""
import json

from scraper import *


def _set_nhl_data(url):
    """Creates a dictionary with keys being each division which map to a list of dictionaries
    of teams in that conference

    Returns:
        dictionary: dictionary with keys being each division which map to a list of dictionaries
        with team stats in the division
    """

    table = get_tables(url)[0]
    list = []
    for i in range(len(table)):
        team_name = table[0][i]
        dict = {"title": team_name,
                "record": str(table[2][i]) + "-" + str(table[3][i]) + "-" + str(table[4][i]),
                "image": get_team_logo(team_name),
                "children":""}
        list.append(dict)

    team_dict = {"Central Division": list[2:10],
                 "East Division": list[11:19],
                 "North Division": list[20:27],
                 "West Division": list[28:]}
    return team_dict


def get_nhl_data():
    """returns data from NHL teams"""
    url = "https://www.hockey-reference.com/leagues/NHL_2021.html"
    return _set_nhl_data(url)