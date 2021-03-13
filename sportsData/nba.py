"""
Gets NBA team data by scraping basketball-reference.com
standings

@Title: nba.py
@Author: Ty, Declan, Jack, Mphatso

"""

from scraper import *


def _set_nba_data(url):
    """Creates a dictionary with keys being each conference and values being a list of dictionaries
        of teams in that conference

        Returns:
            dictionary: dictionary with keys being each division which map to a list of dictionaries
            with team stats in the division
        """
    tables = get_tables(url)
    list = []
    for i in tables:
        for idx in range(len(i) - 1):
            team_name = i[0][idx + 1]
            team_dict = {"title": team_name,
                         "record": i[1][idx + 1] + "-" + i[2][idx + 1],
                         "image": get_team_logo(team_name),
                         "children":""}
            list.append(team_dict)

    dict = {"Eastern Conference": list[0:15],
            "Western Conference": list[15:30]}
    return dict


def get_nba_data(year=2021):
    """
    Returns:

    """
    url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(
        year)
    return _set_nba_data(url)
