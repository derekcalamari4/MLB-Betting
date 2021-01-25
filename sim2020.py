import winner
import parseresults2020
import weight2

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR',
         'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA',
         'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']

# simulate 2020 regular szn games to check accuracy of stat weighting
def sim2020_weight1():
    for team in teams:
        count = 0
        total_games = 0
        opponents = parseresults2020.get_opp(team)
        results = parseresults2020.get_results(team)
        for i in range(opponents.__len__()):
            game_winner = winner.game_winner(team, opponents[i])
            result = results[i]
            total_games += 1
            if game_winner == team and result == 1:
                count += 1
            if game_winner == opponents[i] and result == 0:
                count += 1
        return count / total_games
print(sim2020_weight1())

def sim2020_weight2():
    for team in teams:
        count = 0
        total_games = 0
        opponents = parseresults2020.get_opp(team)
        results = parseresults2020.get_results(team)
        for i in range(opponents.__len__()):
            game_winner = weight2.compare_teams(team, opponents[i])
            result = results[i]
            total_games += 1
            if game_winner == team and result == 1:
                count += 1
            elif game_winner == opponents[i] and result == 0:
                count += 1
    return count / total_games
print(sim2020_weight2())