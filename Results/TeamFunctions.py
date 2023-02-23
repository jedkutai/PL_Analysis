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

def match_information():
    pass