SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}


class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, name):
        if name == self.player1_name:
            self.player1_score += 1
        elif name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError(f"Unrecognized player: {name}")

    def score(self):
        is_early_game = self.player1_score < 4 and self.player2_score < 4
        score_difference = abs(self.player1_score - self.player2_score)

        if score_difference == 0:
            return self.equal_scores()
        elif is_early_game and score_difference != 0:
            return self.early_game_score()
        elif not is_early_game and score_difference == 1:
            return self.advantage_score()
        elif not is_early_game and score_difference > 1:
            return self.winning_score()

    def early_game_score(self):
        p1_score = SCORE_NAMES[self.player1_score]
        p2_score = SCORE_NAMES[self.player2_score]
        return p1_score + "-" + p2_score

    def equal_scores(self):
        if self.player1_score < 3:
            return SCORE_NAMES[self.player1_score] + "-All"
        else:
            return "Deuce"

    def advantage_score(self):
        if self.player1_score > self.player2_score:
            return "Advantage " + self.player1_name
        else:
            return "Advantage " + self.player2_name

    def winning_score(self):
        if self.player1_score > self.player2_score:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name
