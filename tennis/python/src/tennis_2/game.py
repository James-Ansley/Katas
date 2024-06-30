from collections.abc import Callable
from typing import Final, Mapping

SEPARATOR: Final[str] = "-"
ALL_SUFFIX: Final[str] = SEPARATOR + "All"
DEUCE: Final[str] = "Deuce"
SCORE_LABELS: Final[Mapping[int, str]] = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
WIN_FORMAT: Final[Callable[[str], str]] = "Win for {}".format
ADVANTAGE_FORMAT: Final[Callable[[str], str]] = "Advantage {}".format


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
        difference = abs(self.player1_points - self.player2_points)
        points_are_equal = self.player1_points == self.player2_points
        is_early_game = self.player1_points < 4 and self.player2_points < 4

        if points_are_equal:
            return self._equal_points_score()
        elif is_early_game and not points_are_equal:
            return self._early_game_score()
        elif difference == 1 and not is_early_game:
            return self._advantage_score()
        elif difference > 1 and not is_early_game:
            return self._winning_score()
        else:
            raise RuntimeError("Unrecognized score state")

    def _winning_score(self):
        if self.player1_points > self.player2_points:
            return WIN_FORMAT(self.player1_name)
        else:
            return WIN_FORMAT(self.player2_name)

    def _advantage_score(self):
        if self.player1_points > self.player2_points:
            return ADVANTAGE_FORMAT(self.player1_name)
        else:
            return ADVANTAGE_FORMAT(self.player2_name)

    def _early_game_score(self):
        player1_result = SCORE_LABELS[self.player1_points]
        player2_result = SCORE_LABELS[self.player2_points]
        return player1_result + SEPARATOR + player2_result

    def _equal_points_score(self):
        if self.player1_points < 3:
            return SCORE_LABELS[self.player1_points] + ALL_SUFFIX
        else:
            return DEUCE
