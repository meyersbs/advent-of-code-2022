import sys
SCORE_MAP = { "AX": [4, 4], "AY": [1, 8], "AZ": [7, 3], "BX": [8, 1], "BY": [5, 5], "BZ": [2, 9],
    "CX": [3, 7], "CY": [9, 2], "CZ": [6, 6] }
DETERMINE_HANDS = { "AX": "Z", "AY": "X", "AZ": "Y", "BX": "X", "BY": "Y", "BZ": "Z", "CX": "Y",
    "CY": "Z", "CZ": "X" }
SCORES_PART1 = { "player1": [], "player2": [] }
SCORES_PART2 = { "player1": [], "player2": [] }
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        hands = line.strip("\n").split(" ")
        scores = SCORE_MAP[hands[0] + hands[1]]
        SCORES_PART1["player1"].append(scores[0])
        SCORES_PART1["player2"].append(scores[1])
        scores = SCORE_MAP[hands[0] + DETERMINE_HANDS[hands[0] + hands[1]]]
        SCORES_PART2["player1"].append(scores[0])
        SCORES_PART2["player2"].append(scores[1])
print("Player 1: {} | Player 2: {}".format(sum(SCORES_PART1["player1"]),
    sum(SCORES_PART1["player2"])))
print("Player 1: {} | Player 2: {}".format(sum(SCORES_PART2["player1"]),
    sum(SCORES_PART2["player2"])))
