from TeamSummaryClass import *

def store_data(sf_file, sa_file, storage):
    sf_entry, sa_entry = open(sf_file, "r"), open(sa_file, "r")
    sf_entry.readline(), sa_entry.readline() #Clear headers
    sf_entry.readline(), sa_entry.readline() #Clear headers

    sf_data = sf_entry.readline()
    sa_data = sa_entry.readline()
    while sf_data != "":
        sf = sf_data.split(",") # Split data
        sa = sa_data.split(",")
        team_data = TeamSummary(sf[0], sf[4], sf[3], sf[8], sf[9], sf[16], sf[22], sf[23], sf[27], sa[3], sa[8], sa[9], sa[16], sa[22], sa[23], sa[27])
        storage[sf[0]] = team_data

        sf_data = sf_entry.readline()
        sa_data = sa_entry.readline()

def match_information(match_file, match_dict):
    mf = open(match_file, "r")
    mf.readline() #skip header
    for line in mf:
        d = line.split(",") # d is the data chopped up into a list, im just too lazy to write that a bunch of times
        if d[6] == "":
            continue
        score = d[6].split("-")
        entry = MatchInfo(d[0], d[2], d[4], d[8], score[0], score[1], d[5], d[7], d[11])
        name = d[2]+d[4]+d[8]
