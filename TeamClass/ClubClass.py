class Club:
    def __init__(self, club_name):
        self.club_name = club_name
        self.ranking = 0
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

        self.home_games_played = 0
        self.home_goals_scored = []
        self.home_goals_conceded = []
        self.home_goal_difference = 0
        self.home_avg_goals_scored = None
        self.home_avg_goals_conceded = None
        self.home_wins = 0
        self.home_draws = 0
        self.home_losses = 0
        self.home_points = 0
        self.home_goals_scored_deviation = None
        self.home_goals_conceded_deviation = None
        self.home_opponents = []
        self.home_matches = {}

        self.away_games_played = 0
        self.away_goals_scored = []
        self.away_goals_conceded = []
        self.away_goal_difference = 0
        self.away_avg_goals_scored = None
        self.away_avg_goals_conceded = None
        self.away_wins = 0
        self.away_draws = 0
        self.away_losses = 0
        self.away_points = 0
        self.away_goals_scored_deviation = None
        self.away_goals_conceded_deviation = None
        self.away_opponents = []
        self.away_matches = {}

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
        self.ranking = self.points + (self.goal_difference / 1000) + (sum(self.goals_scored) / 100000)

    def update_home_statistics(self): # add home_ to variables
        self.home_avg_goals_scored = sum(self.home_goals_scored) / self.home_games_played
        self.home_avg_goals_conceded = sum(self.home_goals_conceded) / self.home_games_played
        home_scored_sum, home_conceded_sum = [], []
        for x in range(self.home_games_played):
            home_scored, home_conceded = self.home_goals_scored[x], self.home_goals_conceded[x]
            home_scored_sum.append((home_scored - self.home_avg_goals_scored)**2)
            home_conceded_sum.append((home_conceded - self.home_avg_goals_conceded)**2)
        self.home_goals_scored_deviation = (sum(home_scored_sum)/self.home_games_played)**(.5)
        self.home_goals_conceded_deviation = (sum(home_conceded_sum)/self.home_games_played)**(.5)
        self.home_points = (self.home_wins * 3) + self.home_draws
        self.home_goal_difference = sum(self.home_goals_scored) - sum(self.home_goals_conceded)

    def update_away_statistics(self): # add away_ to variables
        self.away_avg_goals_scored = sum(self.away_goals_scored) / self.away_games_played
        self.away_avg_goals_conceded = sum(self.away_goals_conceded) / self.away_games_played
        away_scored_sum, away_conceded_sum = [], []
        for x in range(self.away_games_played):
            away_scored, away_conceded = self.away_goals_scored[x], self.away_goals_conceded[x]
            away_scored_sum.append((away_scored - self.away_avg_goals_scored)**2)
            away_conceded_sum.append((away_conceded - self.away_avg_goals_conceded)**2)
        self.away_goals_scored_deviation = (sum(away_scored_sum)/self.away_games_played)**(.5)
        self.away_goals_conceded_deviation = (sum(away_conceded_sum)/self.away_games_played)**(.5)
        self.away_points = (self.away_wins * 3) + self.away_draws
        self.away_goal_difference = sum(self.away_goals_scored) - sum(self.away_goals_conceded)

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
        

        self.home_games_played += 1
        self.home_opponents.append(opponent)
        self.home_goals_scored.append(int(goals_scored))
        self.home_goals_conceded.append(int(goals_conceded))
        if goals_scored > goals_conceded:
            self.home_wins += 1
        elif goals_conceded > goals_scored:
            self.home_losses += 1
        elif goals_scored == goals_conceded:
            self.home_draws += 1
        self.update_home_statistics()
        

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

        self.away_games_played += 1
        self.away_opponents.append(opponent)
        self.away_goals_scored.append(int(goals_scored))
        self.away_goals_conceded.append(int(goals_conceded))
        if goals_scored > goals_conceded:
            self.away_wins += 1
        elif goals_conceded > goals_scored:
            self.away_losses += 1
        elif goals_scored == goals_conceded:
            self.away_draws += 1
        self.update_away_statistics()

    def __repr__(self):
        if self.goals_scored > self.goals_conceded:
            intro = "{} score {} goals per match and concede {} goals per match\nThey currently have {} points and a goal difference of +{}".format(self.club_name, round(self.avg_goals_scored, 2), round(self.avg_goals_conceded, 2), self.points, self.goal_difference)
        else:
            intro = "{} score {} goals per match and concede {} goals per match\nThey currently have {} points and a goal difference of {}".format(self.club_name, round(self.avg_goals_scored, 2), round(self.avg_goals_conceded, 2), self.points, self.goal_difference)
        return intro

