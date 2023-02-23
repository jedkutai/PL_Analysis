from TeamSummaryClass import *
from TeamFunctions import *

teams = {} # Dictionary that holds team information

# SF is Stats For, SA is Stats Against
sf_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_for.csv"
sa_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_ag.csv"
store_data(sf_file, sa_file, teams)

