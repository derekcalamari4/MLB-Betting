import pandas

#CHA = CHW, CHN = CHC, NYA = NYY, NYN = NYM, SDN = SDP, SFN = SFG, SLN = STL, TBA = TBR
teams = ['ANA', 'ARI', 'ATL', 'BAL', 'BOS', 'CHA', 'CHN', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCA', 'LAN',
         'MIA', 'MIL', 'MIN', 'NYA', 'NYN', 'OAK', 'PHI', 'PIT', 'SDN', 'SEA', 'SFN', 'SLN', 'TBA', 'TEX',
         'TOR', 'WAS']

#csv length
def csv_length(csv):
    numRows = 0
    for row in open(csv):
        numRows += 1
    return numRows

'''
parse 2020 results / return dictionary: ['team1/team2' : 0 or 1] 
0 = team1 victory
1 = team2 victory
'''
def game_outcomes():
    length = csv_length('data/results2020.csv')
    csv = pandas.read_csv('data/results2020.csv', header=None)
    results = {}
    for row in range(length):
        if csv[9][row] > csv[10][row]:
            results[csv[3][row] + '/' + csv[6][row]] = 0
        elif csv[9][row] < csv[10][row]:
            results[csv[3][row] + '/' + csv[6][row]] = 1
    return results
