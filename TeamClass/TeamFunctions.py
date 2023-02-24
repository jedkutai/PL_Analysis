from LeagueClass import League
from ClubClass import Club
import datetime


def match_information(match_file, match_dict):
    mf = open(match_file, "r")
    mf.readline() #skip header
    for line in mf:
        d = line.split(",") # d is the data chopped up into a list, im just too lazy to write that a bunch of times
        if d[6] == "":
            continue
        score = d[6].split("–")
        entry = MatchInfo(d[0], d[2], d[4], d[8], score[0], score[1], d[5], d[7], d[11])
        name = d[2]+d[4]+d[8]
        match_dict[name] = entry

