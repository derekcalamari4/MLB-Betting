import parse

batting = parse.team_batting()
pitching = parse.team_pitching()
fielding = parse.team_fielding()
war = parse.team_war()


'''
Compare statistics between two teams
'''


def compare_batting(teama, teamb, stat):
    stat_abb = {'H': 0, 'R': 1, 'R/G': 2, 'HR': 3, 'RBI': 4, 'OBP': 5, 'SLG': 6, 'OPS': 7}
    ind = stat_abb[stat]
    team_a = batting[teama][ind]
    team_b = batting[teamb][ind]
    if team_a > team_b:
        return teama
    if teamb > teama:
        return teamb


def compare_pitching(teama, teamb, stat):
    stat_abb = {'RA/G': 0, 'ERA': 1, 'WHIP': 2, 'SO/W': 3, 'BB/9': 4}
    ind = stat_abb[stat]
    team_a = pitching[teama][ind]
    team_b = pitching[teamb][ind]
    if ind != 0 or ind != 1 or ind != 3:
        if team_a > team_b:
            return teama
        else:
            return teamb
    else:
        if teama > teamb:
            return teama
        else:
            return teamb


def compare_war(teama, teamb):
    team_a_war = war[teama]
    team_b_war = war[teamb]
    if team_a_war > team_b_war:
        return teama
    else:
        return teamb


def compare_defef(teama, teamb):
    team_a_defef = fielding[teama]
    team_b_defef = fielding[teamb]
    if team_a_defef > team_b_defef:
        return teama
    else:
        return teamb
