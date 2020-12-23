import parseresults2020
import compare
teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
'''
'Weight' of given statistic is the % of games won by a certain team that also had larger value for a given statistic
'''
#return weight of hits
def get_h_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_h(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()


#return weight of 'runs'
def get_r_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_r(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()


#return weight of 'runs/game'
def get_rg_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_rg(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()


#return weight of 'homeruns'
def get_hr_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_hr(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'runs batted in'
def get_rbi_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_rbi(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'On Base Percentage'
def get_obp_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_obp(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'Slugging Percentage'
def get_slg_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_slg(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'OPS'
def get_ops_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_ops(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'runs allowed / game'
def get_rag_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_rag(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'Earned Runs Allowed'
def get_era_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_era(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'WHIP'
def get_whip_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_whip(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'SO/W'
def get_sow_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_sow(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'WAR'
def get_war_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_war(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()

#return weight of 'DeffEff'
def get_deffef_weight(team):
    weights = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if compare.compare_defEf(team, opp[i]) == team and results[i] == 1:
            weights += 1
    return weights/opp.__len__()













