import sys
with open(sys.argv[1], "r") as f:
    overlaps = { "full": 0, "semi": 0 }
    for line in f.readlines():
        s = line.strip("\n").split(",")
        pair_a = [ i for i in range(int(s[0].split("-")[0]), int(s[0].split("-")[1])+1) ]
        pair_b = [ i for i in range(int(s[1].split("-")[0]), int(s[1].split("-")[1])+1) ]
        bool_a = pair_a[0] <= pair_b[0] and pair_a[-1] >= pair_b[-1]
        bool_b = pair_b[0] <= pair_a[0] and pair_b[-1] >= pair_a[-1]
        if bool_a or bool_b: overlaps["full"] += 1
        if len(list(set(pair_a).intersection(set(pair_b)))) != 0: overlaps["semi"] += 1
    print("Full Overlaps: {}".format(overlaps["full"]))
    print("Semi Overlaps: {}".format(overlaps["semi"]))
