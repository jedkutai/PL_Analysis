class PremierLeague:
    def __init__(self, season):
        self.season = season
        self.clubs = {}

    def add_club(self, club_name, club_object):
        self.clubs[club_name] = club_object

    def get_club(self, club_name):
        return self.clubs[club_name]
    
    def __repr__(self):
        pass


class Club:
    def __init__(self, club_name):
        self.club_name = club_name
        self.games_played = 0
        self.goals_scored = []
        self.goals_conceded = []
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

    def add_home_match(self, opponent, goals_scored, goals_conceded):
        self.games_played += 1
        self.opponents.append(opponent)
        self.goals_scored.append(int(goals_scored))
        self.goals_conceded.append(int(goals_conceded))
        self.update_statistics()

    def add_away_match(self, opponent, goals_scored, goals_conceded):
        self.games_played += 1
        self.opponents.append(opponent)
        self.goals_scored.append(int(goals_scored))
        self.goals_conceded.append(int(goals_conceded))
        self.update_statistics()

    def __repr__(self):
        intro = "{} score {} goals per match and concede {} goals per match.".format(self.club_name, self.avg_goals_scored, self.avg_goals_conceded)        
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