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
                offset = [4, 20, 5, 4, 4, 5, 0, 0, 4, 6, 0]
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
        mf.close()

    def z_scored(self, club_name, goals):
        z_scores = []
        mean = self.get_club(club_name).avg_goals_scored
        deviation = self.get_club(club_name).goals_scored_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))

        mean = self.get_club(club_name).home_avg_goals_scored
        deviation = self.get_club(club_name).home_goals_scored_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))

        mean = self.get_club(club_name).away_avg_goals_scored
        deviation = self.get_club(club_name).away_goals_scored_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))
        return z_scores

    def z_conceded(self, club_name, goals):
        z_scores = []
        mean = self.get_club(club_name).avg_goals_conceded
        deviation = self.get_club(club_name).goals_conceded_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))

        mean = self.get_club(club_name).home_avg_goals_conceded
        deviation = self.get_club(club_name).home_goals_conceded_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))

        mean = self.get_club(club_name).away_avg_goals_conceded
        deviation = self.get_club(club_name).away_goals_conceded_deviation
        z = (goals - mean) / deviation
        z_scores.append(round(z, 2))
        return z_scores

    def z_score_to_odds(self, z_score):
        if z_score > 3.9 or z_score <= -3.9:
            return 0
        z_score = round(z_score, 1)
        z_file = open("/Users/jedkutai/Program/PL_Analysis/TeamData/ztable.csv", "r")
        z_file.readline()
        if z_score > 0:
            for line in z_file.readlines():
                data = line.split(";")
                if float(data[0]) == z_score:
                    return 1 - float(data[1])
        else:
            for line in z_file.readlines():
                data = line.split(";")
                if float(data[0]) == z_score:
                    return float(data[1])
        

    def versus(self, home_team, away_team, max_goals=6):
        odds = {}
        scores = []
        for x in range(max_goals+1):
            for y in range(max_goals+1):
                scores.append((x,y))
        for score in scores:
            home_z_scored = self.z_scored(home_team, score[0])
            away_z_conceded = self.z_conceded(away_team, score[0])
            home_z_conceded = self.z_conceded(home_team, score[1])
            away_z_scored = self.z_scored(away_team, score[1])
            a = self.z_score_to_odds(home_z_scored[0])
            b = self.z_score_to_odds(away_z_conceded[0])
            c = self.z_score_to_odds(home_z_conceded[0])
            d = self.z_score_to_odds(away_z_scored[0])
            chance = ((a + b)/2) * ((c + d)/2)
            odds[score] = chance
        odds_sorted = sorted(odds.items(), key=lambda x: x[1], reverse=True)
        xyz = 0
        print("\nTop 5 Results")
        for x in odds_sorted:
            xyz += 1
            ranked = "(H) {} {}-{} (A) {} => {}%".format(home_team, x[0][0], x[0][1], away_team, round((x[1]*100), 2))
            print(ranked)
            if xyz == 5:
                break

    def __repr__(self):
        return self.league_name