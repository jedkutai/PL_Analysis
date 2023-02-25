sort_me = { 1: "5", 5: "1", 2: "4", 4: "2", 3: "3"}
sort_me2 = [(1,5), (1,3), (1,1), (1,2), (1,4)]
i_did = sorted(sort_me.items(), key=lambda x:x[1], reverse=False) 

print(i_did)