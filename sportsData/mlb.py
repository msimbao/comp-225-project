"""
Gets MLB team data by using pybaseball api which scrapes
baseball-reference.com standings page

@Title: mlb.py
@Author: Ty, Declan, Jack, Mphatso

"""
from pybaseball import standings
from scraper import *


def _set_team_list(year):
    """ Creates a list of dictionaries of the team containing data

        Params:
            year(int): year for which season data is wanted

        Returns:
            a list of dictionaries of teams that contains team name, record, logo url
    """
    table = standings(year)
    team_list = []
    for division in table:
        for ind in range(len(division)):
            team_name = division["Tm"][ind + 1]
            team_dict = {"title": team_name,
                         "record": division["W"][ind + 1] + "-" + division["L"][ind+1],
                         "image": get_team_logo(team_name),
                         "children":""}
            team_list.append(team_dict)
    return team_list


def _set_divisions(year):
    """Creates a dictionary with keys being each division which map to a list of dictionaries
        of teams in that conference

        Params:
            year(int): year for which season data is wanted

        Returns:
            dictionary: dictionary with keys being each division which map to a list of dictionaries
            with team stats in the division
            """
    team_list = _set_team_list(year)
    division_dict = {"AL East": team_list[0:5],
                     "AL Central": team_list[5:10],
                     "AL West": team_list[10:15],
                     "NL East": team_list[15:20],
                     "NL Central": team_list[20:25],
                     "NL West": team_list[25:30]}
    return division_dict


def get_mlb_data(year=2020):
    return _set_divisions(year)
