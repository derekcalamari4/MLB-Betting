import parse

batting = parse.teamBatting()
pitching = parse.teamPitching()
fielding = parse.teamFielding()
war = parse.teamWar()


# hits
def compare_h(teama, teamb):
    team_a_h = batting[teama][0]
    team_b_h = batting[teamb][0]
    if team_a_h > team_b_h:
        return teama
    else:
        return teamb


# runs
def compare_r(teama, teamb):
    team_a_r = batting[teama][1]
    team_b_r = batting[teamb][1]
    if team_a_r > team_b_r:
        return teama
    else:
        return teamb


# Runs/Game
def compare_rg(teama, teamb):
    team_a_rg = batting[teama][2]
    team_b_rg = batting[teamb][2]
    if team_a_rg > team_b_rg:
        return teama
    else:
        return teamb


# Homeruns
def compare_hr(teama, teamb):
    team_a_hr = batting[teama][3]
    team_b_hr = batting[teamb][3]
    if team_a_hr > team_b_hr:
        return teama
    else:
        return teamb


# Runs Batted In
def compare_rbi(teama, teamb):
    team_a_rbi = batting[teama][4]
    team_b_rbi = batting[teamb][4]
    if team_a_rbi > team_b_rbi:
        return teama
    else:
        return teamb


# On Base Percentage
def compare_obp(teama, teamb):
    team_a_obp = batting[teama][5]
    team_b_obp = batting[teamb][5]
    if team_a_obp > team_b_obp:
        return teama
    else:
        return teamb


# Slugging percentage
def compare_slg(teama, teamb):
    team_a_slg = batting[teama][6]
    team_b_slg = batting[teamb][6]
    if team_a_slg > team_b_slg:
        return teama
    else:
        return teamb


# OPS
def compare_ops(teama, teamb):
    team_a_ops = batting[teama][7]
    team_b_ops = batting[teamb][7]
    if team_a_ops > team_b_ops:
        return teama
    else:
        return teamb


# Runs Allowed / Game
def compare_rag(teama, teamb):
    team_a_rag = pitching[teama][0]
    team_b_rag = pitching[teamb][0]
    if team_a_rag < team_b_rag:
        return teama
    else:
        return teamb


# Earned runs allowed
def compare_era(teama, teamb):
    team_a_era = pitching[teama][1]
    team_b_era = pitching[teamb][1]
    if team_a_era < team_b_era:
        return teama
    else:
        return teamb


# WHIP
def compare_whip(teama, teamb):
    team_a_whip = pitching[teama][2]
    team_b_whip = pitching[teamb][2]
    if team_a_whip > team_b_whip:
        return teama
    else:
        return teamb


# SO/W
def compare_sow(teama, teamb):
    team_a_sow = pitching[teama][3]
    team_b_sow = pitching[teamb][3]
    if team_a_sow > team_b_sow:
        return teama
    else:
        return teamb


# BB/9
def compare_bb9(teama, teamb):
    teama_a_bb9 = pitching[4]
    team_b_bb9 = pitching[4]
    if teama_a_bb9 > team_b_bb9:
        return teama
    else:
        return teamb


# WAR
def compare_war(teama, teamb):
    team_a_war = war[teama]
    team_b_war = war[teamb]
    if team_a_war > team_b_war:
        return teama
    else:
        return teamb


# Defensive efficency
def compare_defEf(teama, teamb):
    team_a_defef = fielding[teama]
    team_b_defef = fielding[teamb]
    if team_a_defef > team_b_defef:
        return teama
    else:
        return teamb
