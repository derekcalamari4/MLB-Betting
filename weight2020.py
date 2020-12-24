import parseresults2020
import compare

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
'''
'Weight' of given statistic is the % of 'winning a statistic' / 'winning a game'
'''


# return weight of hits
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
    return weights / wins


# return weight of run
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
    return weights / wins


# return the weight of runs/game
def get_rg_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_rg(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of Homeruns
def get_hr_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_hr(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of Runs Batted In
def get_rbi_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_rbi(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of On Base Percentage
def get_obp_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_obp(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of slugging percentage
def get_slg_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_slg(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of OPS
def get_ops_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_ops(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of runs allowed per game
def get_rag_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_rag(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of Earned Runs Allowed
def get_era_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_era(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of WHIP
def get_whip_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_whip(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of Strikeouts per Walk
def get_sow_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_sow(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of WAR (Wins above replacement)
def get_war_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_war(team, opp[i]) == team:
                weights += 1
    return weights / wins


# return the weight of defensive efficiency
def get_defef_weight(team):
    weights = 0
    wins = 0
    opp = parseresults2020.getopp(team)
    results = parseresults2020.getresults(team)
    for i in range(results.__len__()):
        if results[i] == 1:
            wins += 1
            if compare.compare_defEf(team, opp[i]) == team:
                weights += 1
    return weights / wins


'''
get all weights based on 2020 season {['R'], ['R/G'], ['HR'], ['RBI'], ['OBP'], ['SLG'], ['OPS'], ['RA/G'], ['ERA'], 
['WHIP'], ['SO/W'], ['WAR'], ['DefEF']}

h, r, rg, hr, rbi, obp, slg, ops, rag, era, whip, sow, war, defEf
'''

'''

'''


def get_all_weights():
    stats = ['h', 'r', 'rg', 'hr', 'rbi', 'obp', 'slg', 'ops', 'rag', 'era', 'whip', 'sow', 'war', 'defef']
    store = dict()
    result = dict()
    for stat in stats:
        store[stat] = []
        result[stat] = 0
    for team in teams:
        store['h'].append(get_h_weight(team))
        store['r'].append(get_r_weight(team))
        store['rg'].append(get_rg_weight(team))
        store['hr'].append(get_hr_weight(team))
        store['rbi'].append(get_rbi_weight(team))
        store['obp'].append(get_obp_weight(team))
        store['slg'].append(get_slg_weight(team))
        store['ops'].append(get_ops_weight(team))
        store['rag'].append(get_rag_weight(team))
        store['era'].append(get_era_weight(team))
        store['whip'].append(get_whip_weight(team))
        store['sow'].append(get_sow_weight(team))
        store['war'].append(get_war_weight(team))
        store['defef'].append(get_defef_weight(team))
    for stat in store:
        result[stat] = get_avg(store[stat])


# helper method
def get_avg(weights):
    store = 0
    count = 0
    for item in weights:
        count += 1
        store += item
    return store / count
