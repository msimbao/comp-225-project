"""
Gets NFL team data by scraping pro-football-reference.com
standings

@Title: nfl.py
@Author: Ty, Declan, Jack, Mphatso

"""

from scraper import *


def _set_nfl_data(url):
    """"""
    afc_table = get_tables(url)[0]
    nfc_table = get_tables(url)[1]

    afc_dict = _get_conference_dict(afc_table, "AFC")
    nfc_dict = _get_conference_dict(nfc_table, "NFC")

    return {**afc_dict, **nfc_dict}


def _get_conference_dict(table, conference):
    list = []
    for i in range(len(table)):
        team_dict = {"team": table[0][i],
                     "record": str(table[1][i]) + "-" + str(table[2][i])}
        list.append(team_dict)

    league_dict = {"{} East".format(conference): list[2:6],
                   "{} North".format(conference): list[7:11],
                   "{} South".format(conference): list[12:16],
                   "{} West".format(conference): list[17:21]}

    return league_dict


def get_nfl_data(year=2020):
    url = "https://www.pro-football-reference.com/years/{}/".format(year)
    return _set_nfl_data(url)
