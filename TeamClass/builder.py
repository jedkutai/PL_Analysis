from LeagueClass import League
from ClubClass import Club

EPL_2223 = League("Premier League", "2022-2023", 20)
data_file = "/Users/jedkutai/Program/PL_Analysis/TeamData/MatchResults.csv"
EPL_2223.update_clubs(data_file)
print(EPL_2223.clubs.keys())


