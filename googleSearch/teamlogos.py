import requests

from NewsToJson import *


def clean_team_list(team_list):
    league_dict = {}
    league = ""
    for i in team_list:
        if type(i) == str:
            league_dict[i] = []
            league = i
        if type(i) == list:
            league_dict[league] = i

    return league_dict


def clean_dict(league_dict):
    for i in league_dict:
        for j in league_dict[i]:
            print(j)


def get_team_logo(team_name):
    if team_name != "[":
        print(team_name)
        team_name = team_name.replace(" ", "+")
        url = "https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t={}".format(team_name)
        response = requests.get(url)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        return json.loads(search_results)["teams"][0]['strTeamBadge']


def set_team_logo():
    MLB = NLE[1:] + NLC[1:] + NLW[1:] + ALE[1:] + ALC[1:] + ALW[1:]

    NBA = ECATLANTA[1:] + ECCENTRAL[1:] + ECSOUTHEAST[1:] + WCNORTHEAST[1:] + WCPACIFIC[1:] + WCSOUTHWEST[1:]

    NFL = AFCEAST[1:] + AFCNORTH[1:] + AFCSOUTH[1:] + AFCWEST[1:] + NFCEAST[1:] + NFCNORTH[1:] + NFCSOUTH[1:] + NFCWEST[1:]

    NHL = ECATLANTIC[1:] + ECMETROPOLOTAN[1:] + WCPACIFICNHL[1:] + WCCENTRAL[1:]

    league_teams = [NBA, NFL, NHL, MLB]
    logo_dict = {}
    for j in league_teams:
        for i in j:
            logo_dict[i] = get_team_logo(i)

    return logo_dict


def create_file():
    logo_dict = set_team_logo()
    with open("logoDictionary.py", "w") as f:
        f.write("logo_dict = " + str(logo_dict))

if __name__ == '__main__':
    create_file()