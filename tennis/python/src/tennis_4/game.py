class Game:
    def __init__(self, player_1_name, player_2_name):
        self.server = player_1_name
        self.receiver = player_2_name
        self.server_score = 0
        self.receiver_score = 0

    def won_point(self, player_name):
        if self.server == player_name:
            self.server_score += 1
        elif self.receiver == player_name:
            self.receiver_score += 1
        else:
            raise ValueError(f"Unrecognized player name: {player_name}")

    def score(self):
        if self.is_deuce():
            return TennisResult.deuce()
        elif self.server_has_won():
            return TennisResult.win_for(self.server)
        elif self.receiver_has_won():
            return TennisResult.win_for(self.receiver)
        elif self.server_has_advantage():
            return TennisResult.advantage_for(self.server)
        elif self.receiver_has_advantage():
            return TennisResult.advantage_for(self.receiver)
        else:
            return TennisResult.score(self.server_score, self.receiver_score)

    def receiver_has_advantage(self):
        return (
              self.receiver_score >= 4
              and (self.receiver_score - self.server_score) == 1
        )

    def server_has_advantage(self):
        return (
              self.server_score >= 4
              and (self.server_score - self.receiver_score) == 1
        )

    def receiver_has_won(self):
        return (
              self.receiver_score >= 4
              and (self.receiver_score - self.server_score) >= 2
        )

    def server_has_won(self):
        return (
              self.server_score >= 4
              and (self.server_score - self.receiver_score) >= 2
        )

    def is_deuce(self):
        return (
              self.server_score >= 3
              and self.receiver_score >= 3
              and (self.server_score == self.receiver_score)
        )


class TennisResult:
    @classmethod
    def win_for(cls, player):
        return "Win for " + player

    @classmethod
    def advantage_for(cls, player):
        return "Advantage " + player

    @classmethod
    def deuce(cls):
        return "Deuce"

    @classmethod
    def score(cls, player_1_score, player_2_score):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        if scores[player_1_score] == scores[player_2_score]:
            return scores[player_1_score] + "-All"
        else:
            return scores[player_1_score] + "-" + scores[player_2_score]
