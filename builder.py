f = open("/Users/jedkutai/Program/PL_Analysis/Team_Data/Stats_for.txt", "r")
trash = f.readline()
topics = f.readline().split(",")
for x in range(len(topics)):
    print("{} - {}".format(x, topics[x]))