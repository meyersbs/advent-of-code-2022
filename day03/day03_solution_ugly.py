import sys
PRIORITY_MAP = {}
rucksacks, groups, contents = [], [], []
KEYS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for count, key in enumerate(KEYS): PRIORITY_MAP.update({key: count+1})
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        contents.append([l for l in line.strip("\n")])
        rucksacks.append([contents[-1][:len(contents[-1])//2], contents[-1][len(contents[-1])//2:]])
        rucksacks[-1].append(PRIORITY_MAP[list(set(rucksacks[-1][0]) & set(rucksacks[-1][1]))[0]])
    groups = [contents[pos:pos + 3] for pos in range(0, len(contents), 3)]
    badges = [PRIORITY_MAP[list(set(g[0]).intersection(set(g[1])).intersection(set(g[2])))[0]] for g in groups]
    print("Priority Sum: {}".format(sum([r[2] for r in rucksacks])))
    print("Badge Priroity Sum: {}".format(sum(badges)))
