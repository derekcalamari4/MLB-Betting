import pandas
import scrapdata

def csv_length(csv):
    numRows = 0
    for row in open(csv):
        numRows += 1
    return numRows


'''
parse and return dictionary with key: team, values: statistics 
'''


def team_batting():
    scrapdata.batting_csv()
    teams = []
    length = csv_length('batting.csv')
    batting = pandas.read_csv('batting.csv')
    output = {}

    for i in range(length - 1):
        team = batting['Tm'][i]
        if team not in teams:
            teams.append(team)
            output[batting['Tm'][i]] = [batting['H'][i], batting['R'][i], batting['R/G'][i],
                                        batting['HR'][i], batting['RBI'][i], batting['OBP'][i],
                                        batting['SLG'][i], batting['OPS'][i]]
    return output


def team_pitching():
    scrapdata.pitching_csv()
    teams = []
    length = csv_length('pitching.csv')
    pitching = pandas.read_csv('pitching.csv')
    output = {}

    for i in range(length - 1):
        team = pitching['Tm'][i]
        if team not in teams:
            teams.append(team)
            output[pitching['Tm'][i]] = [pitching['RA/G'][i], pitching['ERA'][i], pitching['WHIP'][i],
                                         pitching['SO/W'][i], pitching['BB9'][i]]
    return output


def team_war():
    scrapdata.war_csv()
    teams = []
    length = csv_length('war.csv')
    war = pandas.read_csv('war.csv')
    output = {}

    for i in range(length-1):
        if isinstance(war['Total'][i], str):
            team = war['Total'][i]
            if team not in teams:
                teams.append(team.split(' ')[0])
                output[str(team).split(' ')[0]] = str(team).split(' ')[1]
    return output


def team_fielding():
    scrapdata.fielding_csv()
    teams = []
    length = csv_length('fielding.csv')
    fielding = pandas.read_csv('fielding.csv')
    output = {}

    for i in range(length - 1):
        team = fielding['Tm'][i]
        if team not in teams:
            teams.append(team)
            output[fielding['Tm'][i]] = [fielding['DefEff'][i]]
    return output
