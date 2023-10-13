# -*- coding: utf-8 -*-
import abc
from abc import abstractmethod
from typing import override

SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame4:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if self.player1_name == player_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        rules = self.make_score_rules([
            Deuce,
            EqualScoresNotDeuce,
            Player1Advantage,
            Player2Advantage,
            Player1Win,
            Player2Win,
        ])
        result = rules.get_result()
        return result.format(self.player1_name, self.player2_name)

    def make_score_rules(self, rules):
        rule = DefaultResult(self.player1_score, self.player2_score)
        for new_rule in reversed(rules):
            rule = new_rule(self.player1_score, self.player2_score, rule)
        return rule


class TennisResult:
    def __init__(self, score_format_string):
        self.score_format_string = score_format_string

    def format(self, player1_name: str, player2_name: str):
        return self.score_format_string.format(
            player1=player1_name,
            player2=player2_name,
        )


class ScoreRule(abc.ABC):
    def __init__(
          self,
          player1_score: int,
          player2_score: int,
          next_result: "ScoreRule" = None
    ):
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.next_result = next_result

    def get_result(self):
        if self.is_satisfied():
            return self.score()
        else:
            return self.next_result.get_result()

    @abstractmethod
    def score(self):
        ...

    @abstractmethod
    def is_satisfied(self):
        pass


class Deuce(ScoreRule):
    @override
    def score(self):
        return TennisResult("Deuce")

    @override
    def is_satisfied(self):
        return (
              self.player1_score >= 3 and self.player2_score >= 3
              and (self.player1_score == self.player2_score)
        )


class Player1Win(ScoreRule):
    @override
    def score(self):
        return TennisResult("Win for {player1}")

    @override
    def is_satisfied(self):
        return (
              self.player1_score >= 4
              and (self.player1_score - self.player2_score) >= 2
        )


class Player2Win(ScoreRule):
    @override
    def score(self):
        return TennisResult("Win for {player2}")

    @override
    def is_satisfied(self):
        return (
              self.player2_score >= 4
              and (self.player2_score - self.player1_score) >= 2
        )


class Player1Advantage(ScoreRule):
    @override
    def score(self):
        return TennisResult("Advantage {player1}")

    @override
    def is_satisfied(self):
        return (
              self.player1_score >= 4
              and (self.player1_score - self.player2_score) == 1
        )


class Player2Advantage(ScoreRule):
    @override
    def score(self):
        return TennisResult("Advantage {player2}")

    @override
    def is_satisfied(self):
        return (
              self.player2_score >= 4
              and (self.player2_score - self.player1_score) == 1
        )


class EqualScoresNotDeuce(ScoreRule):
    def score(self):
        return TennisResult(SCORE_NAMES[self.player1_score] + "-All")

    def is_satisfied(self):
        return (
              self.player1_score == self.player2_score
              and self.player1_score < 3
              and self.player2_score < 3
        )


class DefaultResult(ScoreRule):
    @override
    def score(self):
        return TennisResult(
            SCORE_NAMES[self.player1_score]
            + "-"
            + SCORE_NAMES[self.player2_score],
        )

    @override
    def is_satisfied(self):
        return True
