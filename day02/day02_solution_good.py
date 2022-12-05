#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################
SCORE_MAP = {
    "A": 1, "X": 1,
    "B": 2, "Y": 2,
    "C": 3, "Z": 3
}
LOSS = 0
DRAW = 3
WIN = 6


#### CLASSES #######################################################################################
class Player:
    """
    Player object.
    """
    def __init__(self, hands):
        """
        Each player has list of hands, a list of scores, and a total score.
        """
        self.hands = hands
        self.scores = list()
        self.total_score = None

    
    def addScore(self, score):
        """
        Add a score to self.scores.
        """
        self.scores.append(score)


    def totalScore(self):
        self.total_score = sum(self.scores)
        return self.total_score


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in the input data.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            # Strip newlines and split on spaces
            temp_line = line.strip("\n").split(" ")
            data.append(temp_line)

    return data


def _makePlayers(data):
    """
    Create player objects from raw data.
    """
    player1_hands = list()
    player2_hands = list()
    for line in data:
        player1_hands.append(line[0])
        player2_hands.append(line[1])

    # Create players
    player1 = Player(player1_hands)
    player2 = Player(player2_hands)

    return player1, player2


def _getScores(player1_hand, player2_hand):
    """
    Helper for _playHands(...). Determine player scores for a round.
    """
    player1_score = 0
    player2_score = 0

    # Rock
    if player1_hand == "A":
        # Rock
        if player2_hand == "X":
            player1_score += DRAW
            player2_score += DRAW
        # Paper
        elif player2_hand == "Y":
            player1_score += LOSS
            player2_score += WIN
        # Scissors
        else:
            player1_score += WIN
            player2_score += LOSS
    # Paper
    elif player1_hand == "B":
        # Rock
        if player2_hand == "X":
            player1_score += WIN
            player2_score += LOSS
        # Paper
        elif player2_hand == "Y":
            player1_score += DRAW
            player2_score += DRAW
        # Scissors
        else:
            player1_score += LOSS
            player2_score += WIN
    # Scissors
    else:
        # Rock
        if player2_hand == "X":
            player1_score += LOSS
            player2_score += WIN
        # Paper
        elif player2_hand == "Y":
            player1_score += WIN
            player2_score += LOSS
        # Scissors
        else:
            player1_score += DRAW
            player2_score += DRAW

    player1_score += SCORE_MAP[player1_hand]
    player2_score += SCORE_MAP[player2_hand]

    return player1_score, player2_score


def _determineHand(player1_hand, player2_hand):
    """
    Determine what hand Player 2 needs to play.
    """
    # Rock
    if player1_hand == "A":
        # Lose
        if player2_hand == "X":
            return "Z" # Scissors
        # Draw
        elif player2_hand == "Y":
            return "X" # Rock
        # Win
        else:
            return "Y" # Paper
    # Paper
    elif player1_hand == "B":
        # Lose
        if player2_hand == "X":
            return "X" # Rock
        # Draw
        elif player2_hand == "Y":
            return "Y" # Paper
        # Win
        else:
            return "Z" # Scissors
    # Scissors
    else:
        # Lose
        if player2_hand == "X":
            return "Y" # Paper
        # Draw
        elif player2_hand == "Y":
            return "Z" # Scissors
        # Win
        else:
            return "X" # Rock


def _playHands(player1, player2, determineHands=False):
    """
    Play every round of the game and update player scores.
    """
    # For every round
    for i in range(0, len(player1.hands)):
        player1_hand = player1.hands[i]
        player2_hand = player2.hands[i]

        if determineHands:
            player2_hand = _determineHand(player1_hand, player2_hand)

        # Get scores for round
        player1_score, player2_score = _getScores(player1_hand, player2_hand)

        # Update scores
        player1.addScore(player1_score)
        player2.addScore(player2_score)

    # Get total scores
    player1_total = player1.totalScore()
    player2_total = player2.totalScore()

    return player1_total, player2_total


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]

    # Read in data
    filepath = args[0]
    raw_data = _readData(filepath)

    # Part 1
    player1, player2 = _makePlayers(raw_data)
    player1_score_part1, player2_score_part1 = _playHands(player1, player2)

    # Part 2
    player1, player2 = _makePlayers(raw_data)
    player1_score_part2, player2_score_part2 = _playHands(player1, player2, determineHands=True)

    # Print scores
    print("Player 1: {} | Player 2: {}".format(player1_score_part1, player2_score_part1))
    print("Player 1: {} | Player 2: {}".format(player1_score_part2, player2_score_part2))
