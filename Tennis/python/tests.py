# -*- coding: utf-8 -*-

import pytest

from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3
from tennis4 import TennisGame4

test_cases = [
    (0, 0, "player1", "player2", "Love-All"),
    (1, 1, "player1", "player2", "Fifteen-All"),
    (2, 2, "player1", "player2", "Thirty-All"),
    (3, 3, "player1", "player2", "Deuce",),
    (4, 4, "player1", "player2", "Deuce",),
    (1, 0, "player1", "player2", "Fifteen-Love"),
    (0, 1, "player1", "player2", "Love-Fifteen"),
    (2, 0, "player1", "player2", "Thirty-Love"),
    (0, 2, "player1", "player2", "Love-Thirty"),
    (3, 0, "player1", "player2", "Forty-Love"),
    (0, 3, "player1", "player2", "Love-Forty"),
    (4, 0, "player1", "player2", "Win for player1"),
    (0, 4, "player1", "player2", "Win for player2"),
    (2, 1, "player1", "player2", "Thirty-Fifteen"),
    (1, 2, "player1", "player2", "Fifteen-Thirty"),
    (3, 1, "player1", "player2", "Forty-Fifteen"),
    (1, 3, "player1", "player2", "Fifteen-Forty"),
    (4, 1, "player1", "player2", "Win for player1"),
    (1, 4, "player1", "player2", "Win for player2"),
    (3, 2, "player1", "player2", "Forty-Thirty"),
    (2, 3, "player1", "player2", "Thirty-Forty"),
    (4, 2, "player1", "player2", "Win for player1"),
    (2, 4, "player1", "player2", "Win for player2"),
    (4, 3, "player1", "player2", "Advantage player1"),
    (3, 4, "player1", "player2", "Advantage player2"),
    (5, 4, "player1", "player2", "Advantage player1"),
    (4, 5, "player1", "player2", "Advantage player2"),
    (15, 14, "player1", "player2", "Advantage player1"),
    (14, 15, "player1", "player2", "Advantage player2"),
    (6, 4, "player1", "player2", "Win for player1"),
    (4, 6, "player1", "player2", "Win for player2"),
    (16, 14, "player1", "player2", "Win for player1"),
    (14, 16, "player1", "player2", "Win for player2"),
]


def play_game(tennis_game, p1_points, p2_points, p1_name, p2_name):
    game = tennis_game(p1_name, p2_name)
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point(p1_name)
        if i < p2_points:
            game.won_point(p2_name)
    return game


@pytest.mark.parametrize(
    "game_type", [TennisGame1, TennisGame2, TennisGame3, TennisGame4]
)
@pytest.mark.parametrize(
    ("p1_points", "p2_points", "p1_name", "p2_name", "expected_score"),
    test_cases
)
def test_game(
      game_type: type,
      p1_points: int,
      p2_points: int,
      p1_name: str,
      p2_name: str,
      expected_score: str):
    game = play_game(game_type, p1_points, p2_points, p1_name, p2_name)
    assert game.score() == expected_score
