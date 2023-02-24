class League:
    def __init__(self, league_name, season):
        self.league_name = league_name
        self.season = season
        self.clubs = {}

    def add_club(self, club_name, club_object):
        self.clubs[club_name] = club_object

    def get_club(self, club_name):
        return self.clubs[club_name]
    
    def table(self):
        pass # print out clubs ranked

    def __repr__(self):
        return self.league_name


class Club:
    def __init__(self, club_name):
        self.club_name = club_name
        self.games_played = 0
        self.goals_scored = []
        self.goals_conceded = []
        self.goal_difference = 0
        self.avg_goals_scored = None
        self.avg_goals_conceded = None
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0
        self.goals_scored_deviation = None
        self.goals_conceded_deviation = None
        self.opponents = []
        self.matches = {}

    def update_statistics(self):
        self.avg_goals_scored = sum(self.goals_scored) / self.games_played
        self.avg_goals_conceded = sum(self.goals_conceded) / self.games_played
        scored_sum, conceded_sum = [], []
        for x in range(self.games_played):
            scored, conceded = self.goals_scored[x], self.goals_conceded[x]
            scored_sum.append((scored - self.avg_goals_scored)**2)
            conceded_sum.append((conceded - self.avg_goals_conceded)**2)
        self.goals_scored_deviation = (sum(scored_sum)/self.games_played)**(.5)
        self.goals_conceded_deviation = (sum(conceded_sum)/self.games_played)**(.5)
        self.points = (self.wins * 3) + self.draws
        self.goal_difference = sum(self.goals_scored) - sum(self.goals_conceded)

    def add_home_match(self, opponent, goals_scored, goals_conceded):
        self.games_played += 1
        self.opponents.append(opponent)
        self.goals_scored.append(int(goals_scored))
        self.goals_conceded.append(int(goals_conceded))
        if goals_scored > goals_conceded:
            self.wins += 1
        elif goals_conceded > goals_scored:
            self.losses += 1
        elif goals_scored == goals_conceded:
            self.draws += 1
        self.update_statistics()
        

    def add_away_match(self, opponent, goals_scored, goals_conceded):
        self.games_played += 1
        self.opponents.append(opponent)
        self.goals_scored.append(int(goals_scored))
        self.goals_conceded.append(int(goals_conceded))
        if goals_scored > goals_conceded:
            self.wins += 1
        elif goals_conceded > goals_scored:
            self.losses += 1
        elif goals_scored == goals_conceded:
            self.draws += 1
        self.update_statistics()

    def __repr__(self):
        intro = "{} score {} goals per match and concede {} goals per match\nThey currently have {} points and a Goal Difference of: {}".format(self.club_name, round(self.avg_goals_scored, 2), round(self.avg_goals_conceded, 2), self.points, self.goal_difference)        
        return intro



class MatchInfo:
    def __init__(self, match_week, date, home, away, score, home_xG, away_xG, referee):
        self.match_week = match_week
        self.date = date
        self.home = home
        self.away = away
        self.score = score
        self.home_xG = float(home_xG)
        self.away_xG = float(away_xG)
        self.referee = referee

    def __repr__(self): 
        return "{} => (H) {} vs. (A) {} finished {}. {} officiated the match.".format(self.date, self.home, self.away, self.score, self.referee)
    

class Referee:
    pass