import parseresults2020
import compare
teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
'''
'Weight' of given statistic is the % of 'winning a statistic' / 'winning a game'
'''
#return weight of hits
def get_h_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_h(team, opp[i]) == team:
                weights += 1
    return weights/wins

#return weight of run
def get_r_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_r(team, opp[i]) == team:
                weights += 1
    return weights/wins















