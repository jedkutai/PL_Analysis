from LeagueClass import League
from ClubClass import Club

# Premier League
EPL_2223 = League("Premier League", "2022-2023", 20)
data_file = "/Users/jedkutai/Program/PL_Analysis/TeamData/PL_MatchResults_2223.csv"
EPL_2223.update_clubs(data_file)

LaLiga_2223 = League("La Liga", "2022-2023", 20)
liga_file = "/Users/jedkutai/Program/PL_Analysis/TeamData/La_Liga_MatchResults_2223.csv"
LaLiga_2223.update_clubs(liga_file)


print(EPL_2223.table())
print(LaLiga_2223.table())
