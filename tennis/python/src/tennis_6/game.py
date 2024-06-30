class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError("Unrecognized player name")

    def score(self):
        if self.player1_score == self.player2_score:
            return self._tie_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._end_game_score()
        else:
            return self._early_game_score()

    def _early_game_score(self):
        score1 = score_name(self.player1_score)
        score2 = score_name(self.player2_score)
        return score1 + "-" + score2

    def _end_game_score(self):
        if self.player1_score - self.player2_score == 1:
            return "Advantage " + self.player1_name
        elif self.player1_score - self.player2_score == -1:
            return "Advantage " + self.player2_name
        elif self.player1_score - self.player2_score >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def _tie_score(self):
        if self.player1_score < 3:
            return score_name(self.player1_score) + "-All"
        else:
            return "Deuce"


def score_name(score):
    match score:
        case 0:
            return "Love"
        case 1:
            return "Fifteen"
        case 2:
            return "Thirty"
        case 3:
            return "Forty"
