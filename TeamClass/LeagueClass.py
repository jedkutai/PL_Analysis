from ClubClass import Club

class League:
    def __init__(self, league_name, season, max_size):
        self.league_name = league_name
        self.max_size = max_size
        self.size = 0
        self.season = season
        self.clubs = {}

    def add_club(self, club_name, club_object):
        self.clubs[club_name] = club_object
        self.size += 1

    def get_club(self, club_name):
        return self.clubs[club_name]
    
    def table(self):
        t = sorted(self.clubs.values(), key=lambda x: x.ranking, reverse=True)
        ranked_table = ""
        for x in range(len(t)):
            if t[x].goal_difference > 0:
                row = "\n{} {} PL: {} W: {} D: {} L: {} +/-: {}-{} GD: +{} PTS: {}".format(x+1, t[x].club_name, t[x].games_played, t[x].wins, t[x].draws, t[x].losses, sum(t[x].goals_scored), sum(t[x].goals_conceded), t[x].goal_difference, t[x].points)
            else:
                row = "\n{} {} PL: {} W: {} D: {} L: {} +/-: {}-{} GD: {} PTS: {}".format(x+1, t[x].club_name, t[x].games_played, t[x].wins, t[x].draws, t[x].losses, sum(t[x].goals_scored), sum(t[x].goals_conceded), t[x].goal_difference, t[x].points)
            ranked_table += row
        return ranked_table
    
    def update_clubs(self, match_file):
        mf = open(match_file, "r")
        mf.readline() # Skip header
        for line in mf:
            d = line.split(",")
            if d[6] == "":
                continue
            if self.size < self.max_size:
                if (d[4] in self.clubs) == False:
                    new_club = Club(d[4])
                    self.add_club(d[4], new_club)
                if (d[8] in self.clubs) == False:
                    new_club = Club(d[8])
                    self.add_club(d[8], new_club)
            s = d[6].split("–") # Score THE "-" is NOT A REGULAR "-"
            self.get_club(d[4]).add_home_match(d[8],s[0],s[1])
            self.get_club(d[8]).add_away_match(d[4],s[1],s[0])

    def __repr__(self):
        return self.league_name