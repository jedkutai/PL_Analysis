from LeagueClass import League
from ClubClass import Club
import datetime


all_prem_clubs_2223 = ["Crystal Palace", "Arsenal", "Fulham", "Liverpool", "Tottenham", "Southampton", "Newcastle Utd", "Nott'ham Forest", "Leeds United", "Wolves", "Bournemouth", "Aston Villa", "Everton", "Chelsea", "Leicester City", "Brentford", "Manchester Utd", "Brighton", "West Ham", "Manchester City"]

EPL_2223 = League("Premier League", "2022-2023") # 2022-23 Premier League Season

for club_name in all_prem_clubs_2223:
    new_club = Club(club_name)
    EPL_2223.add_club(club_name, new_club)

data_file = "/Users/jedkutai/Program/PL_Analysis/TeamData/MatchResults.csv"

# jawn = open(data_file, "r")
# line = jawn.readline().split(",")
# for x in range(len(line)):
#     print("{} - {}".format(x, line[x]))

EPL_2223.update_clubs(data_file) #Put this into Prem Class in the morning
print(EPL_2223.get_club("Manchester City"))
# figure out datetime stuff

