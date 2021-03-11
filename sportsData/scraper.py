"""
Holds functions for scraping team data

@Title: nhl.py
@Author: Ty, Declan, Jack, Mphatso

"""
import json
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


def _get_soup(url):
    """Creates beautiful soup object from hockey reference

    Returns:
        BeautifulSoup: BeautifulSoup object of hockey reference standing page"""

    url = url
    s = requests.get(url).content
    return BeautifulSoup(s, "lxml")


def get_tables(url):
    """creates table of team data

        Args:
            soup (BeautifulSoup): BeautifulSoup object of hockey reference standings page for 2021

        Return:
            dataset (DataFrame): data frame of 2021 nhl team stats"""
    soup = _get_soup(url)
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


def get_team_logo(team_name):
    if team_name != "[":
        team_name = team_name.replace(" ", "+")
        url = "https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t={}".format(team_name)
        response = requests.get(url)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        return json.loads(search_results)["teams"][0]['strTeamBadge']
