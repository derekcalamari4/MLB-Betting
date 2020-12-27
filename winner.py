import weight2020

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']

'''
main interaction with console / determine winner between two teams 
'''


def get_winner():
    teama = input("first team: ")
    teamb = input("second team: ")
    counta = 0
    countb = 0
    offensea = 0
    pitching_defensea = 0
    offenseb = 0
    pitching_defenseb = 0
    wara = 0
    warb = 0
    stat_abb1 = {'H': 0, 'R': 1, 'R/G': 2, 'HR': 3, 'RBI': 4, 'OBP': 5, 'SLG': 6, 'OPS': 7}
    stat_abb2 = {'RA/G': 0, 'ERA': 1, 'WHIP': 2, 'SO/W': 3, 'BB/9': 4}
    if teama not in teams or teamb not in teams:
        print("Enter valid abbreviations for MLB teams")
    for stat in stat_abb1:
        if weight2020.get_batting_weight(teama, stat) > weight2020.get_batting_weight(teamb, stat):
            counta += 1
            offensea += 1
        elif weight2020.get_batting_weight(teamb, stat) > weight2020.get_batting_weight(teama, stat):
            countb += 1
            offenseb += 1
    for stat in stat_abb2:
        if weight2020.get_pitching_weight(teama, stat) > weight2020.get_pitching_weight(teamb, stat):
            counta += 1
            pitching_defensea += 1
        elif weight2020.get_pitching_weight(teamb, stat) > weight2020.get_pitching_weight(teama, stat):
            countb += 1
            pitching_defenseb += 1
    if weight2020.get_war_weight(teama) > weight2020.get_war_weight(teamb):
        counta += 3
        wara += 1
    else:
        countb += 1
        warb += 3
    if weight2020.get_defef_weight(teama) > weight2020.get_defef_weight(teamb):
        counta += 1
        pitching_defensea += 1
    else:
        countb += 1
        pitching_defenseb += 1
    if offensea > offenseb:
        print(teama + " is more valued on the offense side")
    if offenseb > offensea:
        print(teamb + " is more valued on the offense side")
    if pitching_defensea > pitching_defenseb:
        print(teama + " is more valued on the defensive side")
    if pitching_defenseb > pitching_defensea:
        print(teamb + " is more valued on the defensive side")
    if wara > warb:
        print(teama + " has a higher WAR")
    if warb > wara:
        print(teamb + " has a higher WAR")
    if counta > countb:
        print("Bet: " + teama)
    if countb > counta:
        print("Bet: " + teamb)
    if counta == countb:
        print("Bet: None")
