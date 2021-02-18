"""
Gets NBA team data by scraping basketball-reference.com
standings

@Title: nba.py
@Author: Ty, Declan, Jack, Mphatso

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


def _get_soup(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'.format(year)
    s = requests.get(url).content
    return BeautifulSoup(s, "lxml")


def _get_tables(soup):
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
    s = str(bs4_element)
    start = s.find(">") + 1
    end = s.find("</a>")
    team_name = s[start:end]
    return team_name


def _set_nba_data(year):
    soup = _get_soup(year)
    tables = _get_tables(soup)
    list = []
    for conference in tables:
        for idx in range(len(conference) - 1):
            team_dict = {"team": conference[0][idx + 1],
                         "record": conference[1][idx + 1] + "-" + conference[2][idx + 1]}
            list.append(team_dict)

    dict = {"Eastern Conference": list[0:15],
            "Western Conference": list[15:30]}
    return dict


def get_nba_data(year=2021):
    return _set_nba_data(year)


print(get_nba_data())
