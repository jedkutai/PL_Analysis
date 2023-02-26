def z_score_to_odds(z_score):
        if z_score >= 4 or z_score <= -4:
            return 0
        z_score = round(z_score, 1)
        z_file = open("/Users/jedkutai/Program/PL_Analysis/TeamData/ztable.csv", "r")
        z_file.readline()
        for line in z_file.readlines():
            data = line.split(";")
            if float(data[0]) == z_score:
                return float(data[1])
            

print(z_score_to_odds(-1.9))

tup = {(1,7): 4, (1,0): 42, (2,2): 14}
print(sorted(tup.items(), reverse=True, key=lambda x: x[1]))
sorted_tup = sorted(tup.items(), reverse=True, key=lambda x: x[1])
print(sorted_tup[0][0][1])