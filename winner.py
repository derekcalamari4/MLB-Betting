import weight2020

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']


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
    if teama not in teams or teamb not in teams:
        print("Enter valid abbreviations for MLB teams")
    if weight2020.get_h_weight(teama) > weight2020.get_h_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_r_weight(teama) > weight2020.get_r_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_rg_weight(teama) > weight2020.get_rg_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_hr_weight(teama) > weight2020.get_hr_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_rbi_weight(teama) > weight2020.get_rbi_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_obp_weight(teama) > weight2020.get_obp_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_slg_weight(teama) > weight2020.get_slg_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_ops_weight(teama) > weight2020.get_ops_weight(teamb):
        counta += 1
        offensea += 1
    else:
        countb += 1
        offenseb += 1
    if weight2020.get_rag_weight(teama) > weight2020.get_rag_weight(teamb):
        counta += 1
        pitching_defensea += 1
    else:
        countb += 1
        pitching_defenseb += 1
    if weight2020.get_era_weight(teama) > weight2020.get_era_weight(teamb):
        counta += 1
        pitching_defensea += 1
    else:
        countb += 1
        pitching_defenseb += 1
    if weight2020.get_whip_weight(teama) > weight2020.get_whip_weight(teamb):
        counta += 1
        pitching_defensea += 1
    else:
        countb += 1
        pitching_defenseb += 1
    if weight2020.get_sow_weight(teama) > weight2020.get_sow_weight(teamb):
        counta += 1
        pitching_defensea += 1
    else:
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
