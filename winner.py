import weight2020
import efficiency


teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
stat_abb3 = {'H': 0, 'R': 1, 'R/G': 2, 'HR': 3, 'RBI': 4, 'OBP': 5, 'SLG': 6, 'OPS': 7}
stat_abb4 = {'RA/G': 0, 'ERA': 1, 'WHIP': 2, 'SO/W': 3, 'BB/9': 4}


'''
console comparison
'''


def compare_weights(teama, teamb):
    offense_a = 0
    offense_b = 0
    defense_a = 0
    defense_b = 0
    war_a = 0
    war_b = 0
    for stat in stat_abb3:
        if weight2020.get_batting_weight(teama, stat) > weight2020.get_batting_weight(teamb, stat):
            offense_a += 1
        else:
            offense_b += 1
    for stat in stat_abb4:
        if weight2020.get_pitching_weight(teama, stat) > weight2020.get_pitching_weight(teama, stat):
            defense_a += 1
        else:
            defense_b += 1
    if weight2020.get_war_weight(teama) > weight2020.get_war_weight(teamb):
        war_a += 2
    else:
        war_b += 2
    return offense_a, offense_b, defense_a, defense_b, war_a, war_b


def get_comparison():
    teama = input('first team: ')
    teamb = input('second team: ')

    if teama not in teams or teamb not in teams:
        print('Enter valid abbreviations for MLB teams')
    weights = compare_weights(teama, teamb)
    a_total = 0
    b_total = 0
    if weights[0] > weights[1]:
        a_total += 1
        print('OFF: ' + teama)
    else:
        b_total += 1
        print('OFF: ' + teamb)
    if weights[2] > weights[3]:
        a_total += 1
        print('DEF: ' + teama)
    else:
        b_total += 1
        print('DEF: ' + teamb)
    if weights[4] > weights[5]:
        a_total += 1
        print('WAR: ' + teama)
    else:
        b_total += 1
        print('WAR: ' + teamb)
    print(teama + ' OFF EFF: ' + str(round(efficiency.off_eff(teama), 3)) + ' %')
    print(teama + ' DEF EFF: ' + str(round(efficiency.def_eff(teama), 3)) + ' %')
    print(teamb + ' OFF EFF: ' + str(round(efficiency.off_eff(teamb), 3)) + ' %')
    print(teamb + ' DEF EFF: ' + str(round(efficiency.def_eff(teamb), 3)) + ' %')
    if a_total > b_total:
        print('PROJ WIN: ' + teama)
    elif b_total > a_total:
        print('PROJ WIN: ' + teamb)

get_comparison()
