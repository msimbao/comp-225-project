import json
import requests
import html
import re


class BingSearch:
    def __init__(self, query):
        __articleList = self.__set_up(query)
        self.team_logo_dict = {'Boston Celtics': 'https://www.thesportsdb.com/images/media/team/badge/051sjd1537102179.png', 'Brooklyn Nets': 'https://www.thesportsdb.com/images/media/team/badge/h0dwny1600552068.png', 'New York Knicks': 'https://www.thesportsdb.com/images/media/team/badge/wyhpuf1511810435.png', 'Philadelphia 76ers': 'https://www.thesportsdb.com/images/media/team/badge/71545f1518464849.png', 'Toronto Raptors': 'https://www.thesportsdb.com/images/media/team/badge/gitpi61503743151.png', 'Chicago Bulls': 'https://www.thesportsdb.com/images/media/team/badge/yk7swg1547214677.png', 'Cleveland Cavaliers': 'https://www.thesportsdb.com/images/media/team/badge/a2pp4c1503741152.png', 'Detroit Pistons': 'https://www.thesportsdb.com/images/media/team/badge/12612u1511101660.png', 'Indiana Pacers': 'https://www.thesportsdb.com/images/media/team/badge/v6jzgm1503741821.png', 'Milwaukee Bucks': 'https://www.thesportsdb.com/images/media/team/badge/qgyz6z1503742649.png', 'Atlanta Hawks': 'https://www.thesportsdb.com/images/media/team/badge/c6oi9p1611859646.png', 'Charlotte Hornets': 'https://www.thesportsdb.com/images/media/team/badge/xqtvvp1422380623.png', 'Miami Heat': 'https://www.thesportsdb.com/images/media/team/badge/5v67x51547214763.png', 'Orlando Magic': 'https://www.thesportsdb.com/images/media/team/badge/txuyrr1422492990.png', 'Washington Wizards': 'https://www.thesportsdb.com/images/media/team/badge/m2qhln1503743635.png', 'Denver Nuggets': 'https://www.thesportsdb.com/images/media/team/badge/8o8j5k1546016274.png', 'Minnesota Timberwolves': 'https://www.thesportsdb.com/images/media/team/badge/b6a05s1503742837.png', 'Oklahoma City Thunder': 'https://www.thesportsdb.com/images/media/team/badge/xpswpq1422575434.png', 'Portland Trail Blazers': 'https://www.thesportsdb.com/images/media/team/badge/mbtzin1520794112.png', 'Utah Jazz': 'https://www.thesportsdb.com/images/media/team/badge/9p1e5j1572041084.png', 'Golden State Warriors': 'https://www.thesportsdb.com/images/media/team/badge/irobi61565197527.png', 'Los Angeles Clippers': 'https://www.thesportsdb.com/images/media/team/badge/jv7tf21545916958.png', 'Los Angeles Lakers': 'https://www.thesportsdb.com/images/media/team/badge/44ubym1511102073.png', 'Phoenix Suns': 'https://www.thesportsdb.com/images/media/team/badge/qrtuxq1422919040.png', 'Sacramento Kings': 'https://www.thesportsdb.com/images/media/team/badge/5d3dpz1611859587.png', 'Dallas Mavericks': 'https://www.thesportsdb.com/images/media/team/badge/yqrxrs1420568796.png', 'Houston Rockets': 'https://www.thesportsdb.com/images/media/team/badge/yezpho1597486052.png', 'Memphis Grizzlies': 'https://www.thesportsdb.com/images/media/team/badge/m64v461565196789.png', 'New Orleans Pelicans': 'https://www.thesportsdb.com/images/media/team/badge/f341s31523700397.png', 'San Antonio Spurs': 'https://www.thesportsdb.com/images/media/team/badge/obucan1611859537.png', 'Buffalo Bills': 'https://www.thesportsdb.com/images/media/team/badge/6pb37b1515849026.png', 'Miami Dolphins': 'https://www.thesportsdb.com/images/media/team/badge/trtusv1421435081.png', 'New England Patriots': 'https://www.thesportsdb.com/images/media/team/badge/xtwxyt1421431860.png', 'New York Jets': 'https://www.thesportsdb.com/images/media/team/badge/hz92od1607953467.png', 'Baltimore Ravens': 'https://www.thesportsdb.com/images/media/team/badge/einz3p1546172463.png', 'Cincinnati Bengals': 'https://www.thesportsdb.com/images/media/team/badge/qqtwwv1420941670.png', 'Cleveland Browns': 'https://www.thesportsdb.com/images/media/team/badge/squvxy1420942389.png', 'Pittsburgh Steelers': 'https://www.thesportsdb.com/images/media/team/badge/2975411515853129.png', 'Houston Texans': 'https://www.thesportsdb.com/images/media/team/badge/wqyryy1421436627.png', 'Indianapolis Colts': 'https://www.thesportsdb.com/images/media/team/badge/wqqvpx1421434058.png', 'Jacksonville Jaguars': 'https://www.thesportsdb.com/images/media/team/badge/0mrsd41546427902.png', 'Tennessee Titans': 'https://www.thesportsdb.com/images/media/team/badge/m48yia1515847376.png', 'Denver Broncos': 'https://www.thesportsdb.com/images/media/team/badge/upsspx1421635647.png', 'Kansas City Chiefs': 'https://www.thesportsdb.com/images/media/team/badge/936t161515847222.png', 'Oakland Raiders': 'https://www.thesportsdb.com/images/media/team/badge/xqusqy1421724291.png', 'Los Angeles Chargers': 'https://www.thesportsdb.com/images/media/team/badge/wbhu3a1548320628.png', 'Dallas Cowboys': 'https://www.thesportsdb.com/images/media/team/badge/wrxssu1450018209.png', 'New York Giants': 'https://www.thesportsdb.com/images/media/team/badge/vxppup1423669459.png', 'Philadelphia Eagles': 'https://www.thesportsdb.com/images/media/team/badge/pnpybf1515852421.png', 'Washington Football Team': 'https://www.thesportsdb.com/images/media/team/badge/1m3mzp1595609069.png', 'Chicago Bears': 'https://www.thesportsdb.com/images/media/team/badge/uwtwtv1420941123.png', 'Detroit Lions': 'https://www.thesportsdb.com/images/media/team/badge/lgsgkr1546168257.png', 'Green Bay Packers': 'https://www.thesportsdb.com/images/media/team/badge/rqpwtr1421434717.png', 'Minnesota Vikings': 'https://www.thesportsdb.com/images/media/team/badge/qstqqr1421609163.png', 'Atlanta Falcons': 'https://www.thesportsdb.com/images/media/team/badge/rrpvpr1420658174.png', 'Carolina Panthers': 'https://www.thesportsdb.com/images/media/team/badge/xxyvvy1420940478.png', 'New Orleans Saints': 'https://www.thesportsdb.com/images/media/team/badge/nd46c71537821337.png', 'Tampa Bay Buccaneers': 'https://www.thesportsdb.com/images/media/team/badge/2dfpdl1537820969.png', 'Arizona Cardinals': 'https://www.thesportsdb.com/images/media/team/badge/xvuwtw1420646838.png', 'Los Angeles Rams': 'https://www.thesportsdb.com/images/media/team/badge/8e8v4i1599764614.png', 'San Francisco 49ers': 'https://www.thesportsdb.com/images/media/team/badge/bqbtg61539537328.png', 'Seattle Seahawks': 'https://www.thesportsdb.com/images/media/team/badge/wwuqyr1421434817.png', 'Boston Bruins': 'https://www.thesportsdb.com/images/media/team/badge/vuspuq1421791546.png', 'Buffalo Sabres': 'https://www.thesportsdb.com/images/media/team/badge/qrutxx1426461247.png', 'Detroit Red Wings': 'https://www.thesportsdb.com/images/media/team/badge/1c24ow1546544080.png', 'Florida Panthers': 'https://www.thesportsdb.com/images/media/team/badge/8qtaz11547158220.png', 'Montreal Canadiens': 'https://www.thesportsdb.com/images/media/team/badge/stpryx1421791753.png', 'Ottawa Senators': 'https://www.thesportsdb.com/images/media/team/badge/qurpwu1421616521.png', 'Tampa Bay Lightning': 'https://www.thesportsdb.com/images/media/team/badge/swysut1421791822.png', 'Toronto Maple Leafs': 'https://www.thesportsdb.com/images/media/team/badge/mxig4p1570129307.png', 'Carolina Hurricanes': 'https://www.thesportsdb.com/images/media/team/badge/v07m3x1547232585.png', 'Columbus Blue Jackets': 'https://www.thesportsdb.com/images/media/team/badge/ssytwt1421792535.png', 'New Jersey Devils': 'https://www.thesportsdb.com/images/media/team/badge/ssppey1547160174.png', 'New York Islanders': 'https://www.thesportsdb.com/images/media/team/badge/kj8uh41546001378.png', 'New York Rangers': 'https://www.thesportsdb.com/images/media/team/badge/bez4251546192693.png', 'Philadelphia Flyers': 'https://www.thesportsdb.com/images/media/team/badge/qxxppp1421794965.png', 'Pittsburgh Penguins': 'https://www.thesportsdb.com/images/media/team/badge/dsj3on1546192477.png', 'Washington Capitals': 'https://www.thesportsdb.com/images/media/team/badge/u17iel1547157581.png', 'Anaheim Ducks': 'https://www.thesportsdb.com/images/media/team/badge/6g9t721547289240.png', 'Arizona Coyotes': 'https://www.thesportsdb.com/images/media/team/badge/wpxpsx1421868857.png', 'Calgary Flames': 'https://www.thesportsdb.com/images/media/team/badge/yqptxx1421869532.png', 'Edmonton Oilers': 'https://www.thesportsdb.com/images/media/team/badge/uxxsyw1421618428.png', 'Los Angeles Kings': 'https://www.thesportsdb.com/images/media/team/badge/uvwtvx1421535024.png', 'San Jose Sharks': 'https://www.thesportsdb.com/images/media/team/badge/yui7871546193006.png', 'Vancouver Canucks': 'https://www.thesportsdb.com/images/media/team/badge/xqxxpw1421875519.png', 'Vegas Golden Knights': 'https://www.thesportsdb.com/images/media/team/badge/9w7peh1507632324.png', 'Chicago Blackhawks': 'https://www.thesportsdb.com/images/media/team/badge/tuwyvr1422041801.png', 'Colorado Avalanche': 'https://www.thesportsdb.com/images/media/team/badge/wqutut1421173572.png', 'Dallas Stars': 'https://www.thesportsdb.com/images/media/team/badge/qrvywq1422042125.png', 'Minnesota Wild': 'https://www.thesportsdb.com/images/media/team/badge/swtsxs1422042685.png', 'Nashville Predators': 'https://www.thesportsdb.com/images/media/team/badge/twqyvy1422052908.png', 'St. Louis Blues': 'https://www.thesportsdb.com/images/media/team/badge/rsqtwx1422053715.png', 'Winnipeg Jets': 'https://www.thesportsdb.com/images/media/team/badge/bwn9hr1547233611.png', 'Atlanta Braves': 'https://www.thesportsdb.com/images/media/team/badge/xuwwut1431255795.png', 'Miami Marlins': 'https://www.thesportsdb.com/images/media/team/badge/0722fs1546001701.png', 'New York Mets': 'https://www.thesportsdb.com/images/media/team/badge/rxqspq1431540337.png', 'Philadelphia Phillies': 'https://www.thesportsdb.com/images/media/team/badge/kfq07g1554031454.png', 'Washington Nationals': 'https://www.thesportsdb.com/images/media/team/badge/wpqrut1423694764.png', 'Chicago Cubs': 'https://www.thesportsdb.com/images/media/team/badge/wxbe071521892391.png', 'Cincinnati Reds': 'https://www.thesportsdb.com/images/media/team/badge/wspusr1431538832.png', 'Milwaukee Brewers': 'https://www.thesportsdb.com/images/media/team/badge/08kh2a1595775193.png', 'Pittsburgh Pirates': 'https://www.thesportsdb.com/images/media/team/badge/rtspvy1431538869.png', 'St. Louis Cardinals': 'https://www.thesportsdb.com/images/media/team/badge/uvyvyr1424003273.png', 'Arizona Diamondbacks': 'https://www.thesportsdb.com/images/media/team/badge/sutyqp1431251804.png', 'Colorado Rockies': 'https://www.thesportsdb.com/images/media/team/badge/wvbk1d1550584627.png', 'Los Angeles Dodgers': 'https://www.thesportsdb.com/images/media/team/badge/cgbafw1521896341.png', 'San Diego Padres': 'https://www.thesportsdb.com/images/media/team/badge/t8sl9r1599183156.png', 'San Francisco Giants': 'https://www.thesportsdb.com/images/media/team/badge/mq81yb1521896622.png', 'Baltimore Orioles': 'https://www.thesportsdb.com/images/media/team/badge/ytywvu1431257088.png', 'Boston Red Sox': 'https://www.thesportsdb.com/images/media/team/badge/stpsus1425120215.png', 'New York Yankees': 'https://www.thesportsdb.com/images/media/team/badge/wqwwxx1423478766.png', 'Tampa Bay Rays': 'https://www.thesportsdb.com/images/media/team/badge/littyt1554031623.png', 'Toronto Blue Jays': 'https://www.thesportsdb.com/images/media/team/badge/0v985i1554032049.png', 'Chicago White Sox': 'https://www.thesportsdb.com/images/media/team/badge/yyz5dh1554140884.png', 'Cleveland Indians': 'https://www.thesportsdb.com/images/media/team/badge/fp39hu1521904440.png', 'Detroit Tigers': 'https://www.thesportsdb.com/images/media/team/badge/9dib6o1554032173.png', 'Kansas City Royals': 'https://www.thesportsdb.com/images/media/team/badge/ii3rz81554031260.png', 'Minnesota Twins': 'https://www.thesportsdb.com/images/media/team/badge/necd5v1521905719.png', 'Houston Astros': 'https://www.thesportsdb.com/images/media/team/badge/miwigx1521893583.png', 'Los Angeles Angels': 'https://www.thesportsdb.com/images/media/team/badge/vswsvx1432577476.png', 'Oakland Athletics': 'https://www.thesportsdb.com/images/media/team/badge/wsxtyw1432577334.png', 'Seattle Mariners': 'https://www.thesportsdb.com/images/media/team/badge/39x9ph1521903933.png', 'Texas Rangers': 'https://www.thesportsdb.com/images/media/team/badge/qt9qki1521893151.png'}
        self.__filteredList = self.__filter_articles(__articleList, query)

    def __set_up(self, query):
        list1 = self.__get_from_bing(query, 0)
        list2 = self.__get_from_bing(query, 100)
        return list1["value"] + list2["value"]

    def __get_from_bing(self, query, offset):
        subscription_key = "a18adff624cb4da7a6c9c52a2fc2f28a"
        search_term = query
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term,
                  "count": 100,
                  "offset": offset,
                  "textFormat": "HTML",
                  "mkt": "en-US"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = json.dumps(response.json(), indent=4)
        return json.loads(search_results)

    def __filter_articles(self, articleList, query):
        list = []
        # print(len(articleList))
        news_id = 0
        for i in articleList:
            newDict = {}

            newDict["title"] = html.unescape(i["name"])
            newDict["url"] = i["url"]
            newDict["description"] = html.unescape(i["description"])
            newDict["author"] = html.unescape(i["provider"][0]["name"])
            newDict["id"] = news_id
            newDict["date published"] = i["datePublished"]
            news_id += 1
            try:
                newDict["image"] = i["image"]["thumbnail"]["contentUrl"] + "&h=500&p=0"
            except KeyError:
                try:
                    newDict["image"] = self.team_logo_dict[query]
                except:
                    newDict["image"] = None
            list.append(newDict)

        return sorted(list, key=lambda k: k["date published"], reverse=True)

    def get_article_list(self, n=200):
        if n > len(self.__filteredList):
            return self.__filteredList
        else:
            return self.__filteredList[0:n]


    def __get_object(self, object):
        list = []
        for i in self.__filteredList:
            list.append(i[object])
        return list

    def get_titles(self):
        return self.__get_object("title")

    def get_urls(self):
        return self.__get_object("url")

    def get_images(self):
        return self.__get_object("image")

    def get_description(self):
        return self.__get_object("description")

    def get_author(self):
        return self.__get_object("author")

    def get_ids(self):
        return self.__get_object("id")

    def get_date(self):
        return self.__get_object("date published")


if __name__ == '__main__':
    search = "Tampa Bay Lightning"
    bing_search = BingSearch(search)
    print(bing_search.get_images())
