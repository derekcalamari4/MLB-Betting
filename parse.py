import pandas


def csv_length(csv):
    numRows = 0
    for row in open(csv):
        numRows += 1
    return numRows


'''
parse and return dictionary with key: team, values: statistics 
'''


def team_batting():
    teams = []
    length = csv_length('data/teamstandardbatting.csv')
    batting = pandas.read_csv('data/teamstandardbatting.csv')
    output = {}

    for i in range(length - 1):
        team = batting["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[batting["Tm"][i]] = [batting["H"][i], batting["R"][i], batting["R/G"][i],
                                        batting["HR"][i], batting["RBI"][i], batting["OBP"][i],
                                        batting["SLG"][i], batting["OPS"][i]]
    return output


def team_pitching():
    teams = []
    length = csv_length('data/teamstandardpitching.csv')
    pitching = pandas.read_csv('data/teamstandardpitching.csv')
    output = {}

    for i in range(length - 1):
        team = pitching["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[pitching["Tm"][i]] = [pitching["RA/G"][i], pitching["ERA"][i], pitching["WHIP"][i],
                                         pitching["SO/W"][i], pitching["BB9"][i]]
    return output


def team_war():
    teams = []
    length = csv_length('data/teamwar.csv')
    war = pandas.read_csv('data/teamwar.csv')
    output = {}

    for i in range(length - 1):
        team = war["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[war["Tm"][i]] = war['Total'][i]
    return output


def team_fielding():
    teams = []
    length = csv_length('data/teamfielding.csv')
    fielding = pandas.read_csv('data/teamfielding.csv')
    output = {}

    for i in range(length - 1):
        team = fielding["Tm"][i]
        if team not in teams:
            teams.append(team)
            output[fielding["Tm"][i]] = [fielding['DefEff'][i]]
    return output
