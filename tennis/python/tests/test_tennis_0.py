from pytest import mark

from tennis_0 import Game
from utils import test

from pytest import raises


def set_game(player1, player2, player1_score, player2_score) -> Game:
    game = Game(player1, player2)
    for _ in range(player1_score):
        game.win_point(player1)
    for _ in range(player2_score):
        game.win_point(player2)
    return game


@mark.parametrize(
    ("player1", "player2", "player1_score", "player2_score", "expected"),
    (
          ('player1', 'player2', 0, 1, "Love-Fifteen"),
          ('player1', 'player2', 0, 2, "Love-Thirty"),
          ('player1', 'player2', 0, 3, "Love-Forty"),
          ('player1', 'player2', 1, 0, "Fifteen-Love"),
          ('player1', 'player2', 1, 2, "Fifteen-Thirty"),
          ('player1', 'player2', 1, 3, "Fifteen-Forty"),
          ('player1', 'player2', 2, 0, "Thirty-Love"),
          ('player1', 'player2', 2, 1, "Thirty-Fifteen"),
          ('player1', 'player2', 2, 3, "Thirty-Forty"),
          ('player1', 'player2', 3, 0, "Forty-Love"),
          ('player1', 'player2', 3, 1, "Forty-Fifteen"),
          ('player1', 'player2', 3, 2, "Forty-Thirty"),

    )
)
@test
def scores_display_correctly_for_early_in_progress_games(
      player1, player2, player1_score, player2_score, expected,
):
    game = set_game(player1, player2, player1_score, player2_score)
    assert game.score() == expected


@mark.parametrize(
    ("player1", "player2", "player1_score", "player2_score", "expected"),
    (
          ('player1', 'player2', 0, 0, "Love-All"),
          ('player1', 'player2', 1, 1, "Fifteen-All"),
          ('player1', 'player2', 2, 2, "Thirty-All"),
          ('player1', 'player2', 3, 3, "Deuce"),
          ('player1', 'player2', 4, 4, "Deuce"),
          ('player1', 'player2', 15, 15, "Deuce"),
          ('player1', 'player2', 40, 40, "Deuce"),

    )
)
@test
def scores_are_displayed_correctly_when_equal(
      player1, player2, player1_score, player2_score, expected
):
    game = set_game(player1, player2, player1_score, player2_score)
    assert game.score() == expected


@mark.parametrize(
    ("player1", "player2", "player1_score", "player2_score", "expected"),
    (
          ('playerA', 'playerB', 4, 3, "Advantage playerA"),
          ('playerA', 'playerB', 3, 4, "Advantage playerB"),
          ('playerA', 'playerB', 5, 4, "Advantage playerA"),
          ('playerA', 'playerB', 4, 5, "Advantage playerB"),
          ('playerA', 'playerB', 15, 14, "Advantage playerA"),
          ('playerA', 'playerB', 14, 15, "Advantage playerB"),

    )
)
@test
def scores_are_displayed_with_advantage(
      player1, player2, player1_score, player2_score, expected
):
    game = set_game(player1, player2, player1_score, player2_score)
    assert game.score() == expected


@mark.parametrize(
    ("player1", "player2", "player1_score", "player2_score", "expected"),
    (
          ('playerA', 'player2', 4, 0, "Win for playerA"),
          ('playerA', 'player2', 0, 4, "Win for player2"),
          ('playerA', 'player2', 4, 1, "Win for playerA"),
          ('playerA', 'player2', 1, 4, "Win for player2"),
          ('playerA', 'player2', 4, 2, "Win for playerA"),
          ('player1', 'playerB', 2, 4, "Win for playerB"),
          ('player1', 'playerB', 6, 4, 'Win for player1'),
          ('player1', 'playerB', 4, 6, 'Win for playerB'),
          ('player1', 'playerB', 16, 14, 'Win for player1'),
          ('player1', 'playerB', 14, 16, 'Win for playerB'),
    )
)
@test
def scores_display_correctly_for_completed_games(
      player1, player2, player1_score, player2_score, expected
):
    game = set_game(player1, player2, player1_score, player2_score)
    assert game.score() == expected


@test
def game_throws_on_unrecognised_player():
    game = Game("A", "B")
    with raises(ValueError):
        game.win_point("C")
