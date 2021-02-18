"""
Gets NHL team data by scraping hockey-reference.com
standings

NOTE: only works for 2021 season due to restructuring
of conferences

@Title: nhl.py
@Author: Ty, Declan, Jack, Mphatso

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


def _get_soup():
    """Creates beautiful soup object from hockey reference

    Returns:
        BeautfiulSoup: BeautifulSoup object of hockey reference standing page"""

    url = 'https://www.hockey-reference.com/leagues/NHL_2021_standings.html'
    s = requests.get(url).content
    return BeautifulSoup(s, "lxml")


def _get_tables(soup):
    """creates table of team data

    Args:
        soup (BeautifulSoup): BeautifulSoup object of hockey reference standings page for 2021

    Return:
        dataset (DataFrame): data frame of 2021 nhl team standings"""

    datasets = []
    tables = soup.find_all('table')
    for table in tables:
        data = []
        headings = [th.get_text() for th in table.find("tr").find_all("th")]
        data.append(headings)
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            cols.insert(0, _get_team_name(row.find_all('a')))  # team name
            data.append([ele for ele in cols if ele])
        datasets.append(data)

    datasets = datasets[0:2]
    for idx in range(len(datasets)):
        datasets[idx] = pd.DataFrame(datasets[idx])

    return datasets


def _set_nhl_data():
    """Creates a dictionary with keys being each division which map to a list of dictionaries
    of teams in that conference

    Returns:
        dictionary: dictionary with keys being each division which map to a list of dictionaries
        with team stats in the division
    """

    soup = _get_soup()
    table = _get_tables(soup)[0]
    list = []

    for i in range(len(table)):
        dict = {"Team": table[0][i],
                "Record": str(table[2][i]) + "-" + str(table[3][i]) + "-" + str(table[4][i])}
        list.append(dict)

    team_dict = {"Central Division": list[2:10],
                 "East Division": list[11:19],
                 "North Division": list[20:27],
                 "West Division": list[28:]}
    return team_dict


def _get_team_name(bs4_element):
    """Grabs the team name from HTML

    Args:
        bs4_element: line of HTML containing team name

    Returns:
        string: name of team"""
    s = str(bs4_element)
    start = s.find(">") + 1
    end = s.find("</a>")
    team_name = s[start:end]
    return team_name


def get_nhl_data():
    """returns NHL team data"""
    return _set_nhl_data()


print(get_nhl_data())