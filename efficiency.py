import parse


'''
Return offensive efficiency, defensive efficiency, and total efficiency
'''


def off_eff(team):
    team_lob = parse.team_lob()[team]
    team_runs = parse.team_batting()[team][1]
    return team_runs / (team_lob + team_runs)


def def_eff(team):
    return parse.team_fielding()[team][0]



def tot_eff(team):
    return def_eff(team) + off_eff(team)