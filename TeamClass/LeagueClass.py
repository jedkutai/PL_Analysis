from ClubClass import Club

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