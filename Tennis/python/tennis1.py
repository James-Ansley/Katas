from collections import defaultdict
from collections.abc import Mapping
from typing import Final

SCORE_NAMES: Final[Mapping] = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
EQUAL_POINT_SCORE_NAMES: Final[Mapping] = defaultdict(
    lambda: "Deuce",
    {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }
)
WIN_SCORE_NAME: Final[str] = "Win for {}"
ADVANTAGE_SCORE_NAME: Final[str] = "Advantage {}"


class TennisGame1:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name: Final[str] = player1_name
        self.player2_name: Final[str] = player2_name
        self._player1_points: int = 0
        self._player2_points: int = 0

    @property
    def player1_points(self) -> int:
        """The current points for the first player"""
        return self._player1_points

    @property
    def player2_points(self) -> int:
        """The current points for the second player"""
        return self._player2_points

    @property
    def score_difference(self) -> int:
        """The absolute difference between player scores"""
        return abs(self._player1_points - self._player2_points)

    def won_point(self, player_name: str) -> None:
        """
        Increments the point count for the given player

        :param player_name: The name of the player to award the won point
        :raises ValueError: If the given name does not match either
            player's name
        """
        if player_name == self.player1_name:
            self._player1_points += 1
        elif player_name == self.player2_name:
            self._player2_points += 1
        else:
            raise ValueError("Unrecognized player name")

    def score(self) -> str:
        """Returns the current tennis score name for the game"""
        player_can_win = self._player1_points >= 4 or self._player2_points >= 4
        is_advantage = player_can_win and self.score_difference == 1
        is_win = player_can_win and self.score_difference >= 2

        if self._player1_points == self._player2_points:
            return self.equal_points_score()
        elif is_advantage:
            return self.advantage_score()
        elif is_win:
            return self.win_score()
        else:
            return self.combined_scores()

    def combined_scores(self) -> str:
        return "-".join((
            SCORE_NAMES[self._player1_points],
            SCORE_NAMES[self._player2_points],
        ))

    def advantage_score(self) -> str:
        if self._player1_points > self._player2_points:
            return ADVANTAGE_SCORE_NAME.format(self.player1_name)
        else:
            return ADVANTAGE_SCORE_NAME.format(self.player2_name)

    def win_score(self) -> str:
        if self._player1_points > self._player2_points:
            return WIN_SCORE_NAME.format(self.player1_name)
        else:
            return WIN_SCORE_NAME.format(self.player2_name)

    def equal_points_score(self) -> str:
        return EQUAL_POINT_SCORE_NAMES[self._player1_points]
