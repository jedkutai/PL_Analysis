from TeamSummaryClass import *
from TeamFunctions import *

# SF is stats for, SA is stats against
sf_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_for.txt"
sa_file = "/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_ag.txt"

sf = open(sf_file, "r")
sa = open(sa_file, "r")

sf_header = sf.readline() # Clear topline
sa_header = sa.readline()

sf_topics = sf.readline().split(",") # Clear Second line (topics)
sa_topics = sa.readline().split(",")

for x in range(len(sf_topics)):
    print("{} - {}".format(x, sf_topics[x]))



teams = {} # Dictionary that holds team information
store_data(sf, sa, teams)

print(teams["Arsenal"])