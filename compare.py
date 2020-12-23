import parse

batting = parse.teamBatting()
pitching = parse.teamPitching()
fielding = parse.teamFielding()
war = parse.teamWar()
#hits
def compare_h(teama, teamb):
    team_a_h = batting[teama][0]
    team_b_h = batting[teamb][0]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#runs
def compare_r(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Runs/Game
def compare_rg(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Homeruns
def compare_hr(teama, teamb):
    team_a_h = batting[teama][2]
    team_b_h = batting[teamb][2]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Runs Batted In
def compare_rbi(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#On Base Percentage
def compare_obp(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Slugging percentage
def compare_slg(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#OPS
def compare_ops(teama, teamb):
    team_a_h = batting[teama][1]
    team_b_h = batting[teamb][1]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Runs Allowed / Game
def compare_rag(teama, teamb):
    team_a_h = pitching[teama][0]
    team_b_h = pitching[teamb][0]
    if team_a_h < team_b_h:
        return teama
    else:
        return teamb

#Earned runs allowed
def compare_era(teama, teamb):
    team_a_h = pitching[teama][1]
    team_b_h = pitching[teamb][1]
    if team_a_h < team_b_h:
        return teama
    else:
        return teamb

#WHIP
def compare_whip(teama, teamb):
    team_a_h = pitching[teama][2]
    team_b_h = pitching[teamb][2]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#SO/W
def compare_sow(teama, teamb):
    team_a_h = pitching[teama][3]
    team_b_h = pitching[teamb][3]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#WAR
def compare_war(teama, teamb):
    team_a_h = war[teama][0]
    team_b_h = war[teamb][0]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb

#Defensive efficency
def compare_defEf(teama, teamb):
    team_a_h = batting[teama][0]
    team_b_h = batting[teamb][0]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb



