from ClubClass import Club

class League:
    def __init__(self, league_name, season, max_size=20):
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
        rt = "" # ranked table
        header = "\n\n#   Team" + " "*16 + "PL" + " "*3 + "W" + " "*3 + "D" + " "*3+ "L" + " "*5 + "+/-" + " "*3 + "GD" + " "*4 + "PTS"
        for x in range(len(t)):
            r = ""
            if t[x].goal_difference > 0:
                offset = [4, 20, 5, 4, 4, 5, 0, 0, 4, 6, 20]
                row = [str(x+1), str(t[x].club_name), str(t[x].games_played), str(t[x].wins), str(t[x].draws), str(t[x].losses), str(sum(t[x].goals_scored)), "-", str(sum(t[x].goals_conceded)), "+" + str(t[x].goal_difference), str(t[x].points)]
                for x in range(len(row)):
                    spaces = offset[x] - len(row[x])
                    r += row[x] + " "*spaces
            elif t[x].goal_difference < 0:
                offset = [4, 20, 5, 4, 4, 5, 0, 0, 4, 6, 20]
                row = [str(x+1), str(t[x].club_name), str(t[x].games_played), str(t[x].wins), str(t[x].draws), str(t[x].losses), str(sum(t[x].goals_scored)), "-", str(sum(t[x].goals_conceded)), str(t[x].goal_difference), str(t[x].points)]
                for x in range(len(row)):
                    spaces = offset[x] - len(row[x])
                    r += row[x] + " "*spaces
            else:
                offset = [4, 20, 5, 4, 4, 5, 0, 0, 5, 5, 20]
                row = [str(x+1), str(t[x].club_name), str(t[x].games_played), str(t[x].wins), str(t[x].draws), str(t[x].losses), str(sum(t[x].goals_scored)), "-", str(sum(t[x].goals_conceded)), str(t[x].goal_difference), str(t[x].points)]
                for x in range(len(row)):
                    spaces = offset[x] - len(row[x])
                    r += row[x] + " "*spaces

            rt += "\n" + r
            
        return header + rt
    
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