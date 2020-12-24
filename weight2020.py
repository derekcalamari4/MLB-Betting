import parseresults2020
import compare

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
'''
'Weight' of given statistic is the %: ('winning a statistic' and 'winning a game' / 'winning a game')
'''


def get_batting_weight(team, stat):
    weights = 0
    wins = 0
    opp = parseresults2020.get_opp(team)
    results = parseresults2020.get_results(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_batting(team, opp[i], stat) == team:
                weights += 1
    return weights / wins


def get_pitching_weight(team, stat):
    weights = 0
    wins = 0
    opp = parseresults2020.get_opp(team)
    results = parseresults2020.get_results(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_pitching(team, opp[i], stat) == team:
                weights += 1
    return weights / wins


def get_war_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.get_opp(team)
    results = parseresults2020.get_results(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_war(team, opp[i]) == team:
                weights += 1
    return weights / wins


def get_defef_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.get_opp(team)
    results = parseresults2020.get_results(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_defef(team, opp[i]) == team:
                weights += 1
    return weights / wins
