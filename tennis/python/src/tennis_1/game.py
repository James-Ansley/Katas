from collections.abc import Mapping
from typing import Final

STARTING_SCORE_NAMES: Final[Mapping[int, str]] = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
DEUCE: Final[str] = "Deuce"
EQUAL_POINT_SCORE_NAMES: Final[Mapping[int, str]] = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}


class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1
        else:
            raise ValueError(f"Unrecognized player name: {player_name}")

    def score(self):
        score_difference = abs(self.player1_points - self.player2_points)
        is_late_game = self.player1_points >= 4 or self.player2_points >= 4

        if self.player1_points == self.player2_points:
            return self.equal_point_score()
        elif is_late_game and score_difference == 1:
            return self.advantage_score()
        elif is_late_game and score_difference > 1:
            return self.winning_score()
        else:
            return self.starting_game_score()

    def winning_score(self):
        if self.player1_points > self.player2_points:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def advantage_score(self):
        if self.player1_points > self.player2_points:
            return f"Advantage {self.player1_name}"
        else:
            return f"Advantage {self.player2_name}"

    def starting_game_score(self):
        return (
              STARTING_SCORE_NAMES[self.player1_points]
              + "-"
              + STARTING_SCORE_NAMES[self.player2_points]
        )

    def equal_point_score(self):
        return EQUAL_POINT_SCORE_NAMES.get(self.player1_points, DEUCE)
