from TeamSummaryClass import *
from TeamFunctions import *

# Dictionaries
teams = {}
match_results = {}

# SF is Stats For, SA is Stats Against
sf_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_for.csv"
sa_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_ag.csv"
store_data(sf_file, sa_file, teams)

# Match Results
match_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/MatchResults.csv"
mf = open(match_file, "r")
header = mf.readline().split(",")
for x in range(len(header)):
    print("{} - {}".format(x, header[x]))


match_information(match_file, match_results)