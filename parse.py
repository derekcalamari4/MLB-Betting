import pandas


# return length of given csv file
def csvLength(csv):
    numRows = 0
    for row in open(csv):
        numRows += 1
    return numRows


# parse and return dictionary with key: team, value: [h, r, rg, hr, rbi, obp, slg, ops]
def teamBatting():
    teams = []
    length = csvLength('teamstandardbatting.csv')
    team_batting = pandas.read_csv('teamstandardbatting.csv')
    output = {}

    for i in range(length-1):
        team = team_batting["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[team_batting["Tm"][i]] = [team_batting["H"][i], team_batting["R"][i], team_batting["R/G"][i],
                                             team_batting["HR"][i], team_batting["RBI"][i], team_batting["OBP"][i],
                                             team_batting["SLG"][i], team_batting["OPS"][i]]
    return output


#parse and return dictionary with key: team, value: [RA/G, ERA, WHIP SO/W]
def teamPitching():
    teams = []
    length = csvLength('teamstandardpitching.csv')
    team_pitching = pandas.read_csv('teamstandardpitching.csv')
    output = {}

    for i in range(length-1):
        team = team_pitching["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[team_pitching["Tm"][i]] = [team_pitching["RA/G"][i], team_pitching["ERA"][i], team_pitching["WHIP"][i],
                                              team_pitching["SO/W"][i]]
    return output


#parse and return dictionary with key: team, value: WAR
def teamWar():
    teams = []
    length = csvLength('teamwar.csv')
    team_war = pandas.read_csv('teamwar.csv')
    output = {}

    for i in range(length-1):
        team = team_war["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[team_war["Tm"][i]] = team_war['Total'][i]
    return output


#parse and return dictionary with key: team, value: defEff
def teamFielding():
    teams = []
    length = csvLength('teamfielding.csv')
    team_fielding = pandas.read_csv('teamfielding.csv')
    output = {}

    for i in range(length-1):
        team = team_fielding["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[team_fielding["Tm"][i]] = [team_fielding['DefEff'][i]]
    return output


