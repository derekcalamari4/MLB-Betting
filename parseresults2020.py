import pandas


def csv_length(csv):
    num_rows = 0
    for row in open(csv):
        num_rows += 1
    return num_rows


'''
Parse opponents and results for each MLB team (2020)
'''


def parse(file):
    length = csv_length(file)
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


def get_opp(team):
    return parse('data/' + team + '2020.csv')[0]


def get_results(team):
    return parse('data/' + team + '2020.csv')[1]
