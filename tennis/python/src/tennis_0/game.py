from collections.abc import Callable, Mapping
from typing import Final

DEUCE: Final[str] = "Deuce"
STARTING_SCORE_NAMES: Final[Mapping[int, str]] = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}
STARTING_TIE_SCORE_NAMES: Final[Mapping[int, str]] = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}
STARTING_SCORE_FORMAT: Final[Callable[[str, str], [str]]] = "{}-{}".format
ADVANTAGE_FORMAT: Final[Callable[[str], [str]]] = "Advantage {}".format
WIN_FORMAT: Final[Callable[[str], [str]]] = "Win for {}".format


class Game:
    def __init__(self, player1: str, player2: str):
        self.player1: Final[str] = player1
        self.player2: Final[str] = player2
        self._player1_score = 0
        self._player2_score = 0

    def win_point(self, player: str) -> None:
        if player == self.player1:
            self._player1_score += 1
        elif player == self.player2:
            self._player2_score += 1
        else:
            raise ValueError(f"Unrecognized player: {player}")

    def score(self) -> str:
        is_early_game = self._player1_score < 4 and self._player2_score < 4
        score_difference = abs(self._player1_score - self._player2_score)

        if score_difference == 0:
            return self._equal_scores()
        elif score_difference != 0 and is_early_game:
            return self._starting_scores()
        elif score_difference == 1 and not is_early_game:
            return self._advantage_score()
        elif score_difference > 1 and not is_early_game:
            return self._winning_score()
        else:
            raise RuntimeError(
                f"Unrecognizable score state: "
                f"({self._player1_score}-{self._player2_score})"
            )

    def _starting_scores(self) -> str:
        return STARTING_SCORE_FORMAT(
            STARTING_SCORE_NAMES[self._player1_score],
            STARTING_SCORE_NAMES[self._player2_score],
        )

    def _equal_scores(self) -> str:
        if self._player1_score < 3 and self._player2_score < 3:
            return STARTING_TIE_SCORE_NAMES[self._player1_score]
        else:
            return DEUCE

    def _advantage_score(self) -> str:
        if self._player1_score > self._player2_score:
            return ADVANTAGE_FORMAT(self.player1)
        else:
            return ADVANTAGE_FORMAT(self.player2)

    def _winning_score(self) -> str:
        if self._player1_score > self._player2_score:
            return WIN_FORMAT(self.player1)
        else:
            return WIN_FORMAT(self.player2)
