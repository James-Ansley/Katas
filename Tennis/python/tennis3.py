# -*- coding: utf-8 -*-
SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    @property
    def score_difference(self):
        return abs(self.player1_score - self.player2_score)

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        can_win = self.player1_score >= 4 or self.player2_score >= 4
        scores_equal = self.player1_score == self.player2_score
        is_advantage = can_win and self.score_difference == 1

        if scores_equal:
            return self.equal_points_score()
        elif not can_win:
            return self.combined_scores()
        elif is_advantage:
            return "Advantage " + self.player_in_lead()
        else:
            return "Win for " + self.player_in_lead()

    def combined_scores(self):
        return (
              SCORE_NAMES[self.player1_score]
              + "-"
              + SCORE_NAMES[self.player2_score]
        )

    def equal_points_score(self):
        if self.player1_score >= 3 and self.player2_score >= 3:
            return "Deuce"
        else:
            return SCORE_NAMES[self.player1_score] + "-All"

    def player_in_lead(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        else:
            return self.player2_name
