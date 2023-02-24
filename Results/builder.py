from TeamSummaryClass import *
from TeamFunctions import *

all_prem_clubs_2223 = ["Crystal Palace", "Arsenal", "Fulham", "Liverpool", "Tottenham", "Southampton", "Newcastle Utd", "Nott'ham Forest", "Leeds United", "Wolves", "Bournemouth", "Aston Villa", "Everton", "Chelsea", "Leicester City", "Brentford", "Manchester Utd", "Brighton", "West Ham", "Manchester City"]
EPL_2223 = PremierLeague("2022-2023") # 2022-23 Premier League Season

for club_name in all_prem_clubs_2223:
    new_club = Club(club_name)
    EPL_2223.add_club(club_name, new_club)

data_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/MatchResults.csv"
jawn = open(data_file, "r")
line = jawn.readline().split(",")
for x in range(len(line)):
    print("{} - {}".format(x, line[x]))

update_clubs(data_file, EPL_2223)

print(EPL_2223.get_club("Arsenal"))