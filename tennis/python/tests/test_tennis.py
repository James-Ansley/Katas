from pytest import mark
from pytest import raises

from tennis_1 import Game as Game_1
from tennis_2 import Game as Game_2
from tennis_3 import Game as Game_3
from tennis_4 import Game as Game_4
from tennis_5 import Game as Game_5
from tennis_6 import Game as Game_6
from utils import test


def set_game(game_type, player1, player2, player1_score, player2_score):
    game = game_type(player1, player2)
    for _ in range(player1_score):
        game.won_point(player1)
    for _ in range(player2_score):
        game.won_point(player2)
    return game


@mark.parametrize("game_type", (Game_1, Game_2, Game_3, Game_4, Game_5, Game_6))
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
          ('player1', 'player2', 0, 0, "Love-All"),
          ('player1', 'player2', 1, 1, "Fifteen-All"),
          ('player1', 'player2', 2, 2, "Thirty-All"),
          ('player1', 'player2', 3, 3, "Deuce"),
          ('player1', 'player2', 4, 4, "Deuce"),
          ('player1', 'player2', 15, 15, "Deuce"),
          ('player1', 'player2', 40, 40, "Deuce"),
          ('playerA', 'playerB', 4, 3, "Advantage playerA"),
          ('playerA', 'playerB', 3, 4, "Advantage playerB"),
          ('playerA', 'playerB', 5, 4, "Advantage playerA"),
          ('playerA', 'playerB', 4, 5, "Advantage playerB"),
          ('playerA', 'playerB', 15, 14, "Advantage playerA"),
          ('playerA', 'playerB', 14, 15, "Advantage playerB"),
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
      game_type, player1, player2, player1_score, player2_score, expected
):
    game = set_game(game_type, player1, player2, player1_score, player2_score)
    assert game.score() == expected


@mark.parametrize("game_type", (Game_1, Game_2, Game_3, Game_4, Game_5, Game_6))
@test
def game_throws_on_unrecognised_player(game_type):
    game = game_type("A", "B")
    with raises(ValueError):
        game.won_point("C")
