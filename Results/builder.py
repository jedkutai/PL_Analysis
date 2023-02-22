sf = open("/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_for.txt", "r")
sa = open("/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_ag.txt", "r")

header_sf = sf.readline()
topics_sf = sf.readline().split(",")
for x in range(len(topics_sf)):
    print("{} - {}".format(x, topics_sf[x]))