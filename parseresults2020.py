import pandas


# return length of given csv file
def csvLength(csv):
    numRows = 0
    for row in open(csv):
        numRows += 1
    return numRows


'''
'Tm' 'Opp' 'W/L' (W,L, W-wo) / return team dictionary: key: 'team', value: [opp, 1 (win) or 0 (loss)]
*** Two teams only played 58 games, not 60 ***
'''


def parse(file):
    length = csvLength(file)
    file = pandas.read_csv(file)
    opps = []
    results = []

    for i in range(length - 3):
        opps.append(file['Opp'][i])
        if file['W/L'][i] == 'W' or file['W/L'][i] == 'W-wo':
            results.append(1)
        else:
            results.append(0)
    return opps, results


# return opponents of given team for 2020 szn
def getopp(team):
    return parse('data/' + team + '2020.csv')[0]


# return results of given team for 2020 szn
def getresults(team):
    return parse('data/' + team + '2020.csv')[1]
