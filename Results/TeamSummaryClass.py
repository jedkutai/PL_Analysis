class TeamSummary:
    def __init__(self, team, matches_played, possesion, goals, assists, xGoals, goals_avg, assists_avg, xGoals_avg, possesion_ag, goals_ag, assists_ag, xGoals_ag, goals_avg_ag, assists_avg_ag, xGoals_avg_ag):
        self.team = team
        self.matches_played = int(matches_played)
        self.possesion = float(possesion)
        self.goals = int(goals)
        self.assists = int(assists)
        self.xGoals = float(xGoals)
        self.goals_avg = float(goals_avg)
        self.assists_avg = float(assists_avg)
        self.xGoals_avg = float(xGoals_avg)
        self.possesion_ag = float(possesion_ag)
        self.goals_ag = float(goals_ag)
        self.assists_ag = float(assists_ag)
        self.xGoals_ag = float(xGoals_avg_ag)
        self.goals_avg_ag = float(goals_avg_ag)
        self.assists_avg_ag = float(assists_avg_ag)
        self.xGoals_avg_ag = float(xGoals_avg_ag)

    def __repr__(self):
        intro = "{} have played {} this season in the Premier League\n\n".format(self.team, self.matches_played)
        stats = "Possesion: {}\nGoals: {}\nAssists: {}\nxGoals: {}\nAvg Goals: {}\nAvg Assists: {}\nAvg xGoals: {}\n\n".format(self.possesion, self.goals, self.assists, self.xGoals, self.goals_avg, self.assists_avg, self.xGoals_avg)
        op_intro = "This is how other Premier League Teams perform against {}\n\n".format(self.team)
        op_stats = "Possesion: {}\nGoals: {}\nAssists: {}\nxGoals: {}\nAvg Goals: {}\nAvg Assists: {}\nAvg xGoals: {}\n\n".format(self.possesion_ag, self.goals_ag, self.assists_ag, self.xGoals_ag, self.goals_avg_ag, self.assists_avg_ag, self.xGoals_avg_ag)
        return intro + stats + op_intro + op_stats
    

class MatchInfo:
    def __init__(self, home, away, home_goals, away_goals, home_xG, away_xG, referee):
        self.home = home
        self.away = away
        self.home_goals = int(home_goals)
        self.away_goals = int(away_goals)
        self.home_xG = float(home_xG)
        self.away_xG = float(away_xG)
        self.referee = referee

    def __repr__(self):
        return "(H) {} vs. (A) {} finished {} - {}. {} officiated the match.".format(self.home, self.away, self.home_goals, self.away_goals, self.referee)