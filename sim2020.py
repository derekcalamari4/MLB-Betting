import winner
import parse2020results

teams = ['ANA', 'ARI', 'ATL', 'BAL', 'BOS', 'CHA', 'CHN', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCA', 'LAN',
         'MIA', 'MIL', 'MIN', 'NYA', 'NYN', 'OAK', 'PHI', 'PIT', 'SDN', 'SEA', 'SFN', 'SLN', 'TBA', 'TEX',
         'TOR', 'WAS']
diff_team_names = {'CHA': 'CHW', 'CHN': 'CHC', 'NYA': 'NYY', 'NYN': 'NYM', 'SDN': 'SDP', 'SFN': 'SFG',
                   'SLN': 'STL', 'TBA': 'TBR', 'LAN': 'LAD', 'ANA': 'LAA'}

results = parse2020results.game_outcomes()


# configure proper team names / return new results dictionary
def config_team_names():
    new_results = {}
    key_list = results.keys()
    for key in key_list:
        teama = key.split('/')[0]
        teamb = key.split('/')[1]
        for key2 in diff_team_names.keys():
            if teama == key2:
                teama = diff_team_names[key2]
            if teamb == key2:
                teamb = diff_team_names[key2]
        new_results[teama + '/' + teamb] = results[key]
    return new_results


# simulate 2020 reg szn to check accuracy of winner.py
def sim2020():
    return
