class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        game_can_be_won = self.player1_points >= 4 or self.player2_points >= 4
        points_difference = abs(self.player1_points - self.player2_points)
        is_advantage = game_can_be_won and points_difference == 1
        
        if self.player1_points == self.player2_points:
            return self.equal_points_score()
        elif self.player2_points < 4 and self.player1_points < 4:
            return self.combined_points_score()
        elif is_advantage:
            return self.advantage_score()
        elif game_can_be_won:
            return self.win_score()

    def win_score(self):
        if (self.player1_points - self.player2_points) >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def advantage_score(self):
        if self.player2_points < self.player1_points:
            return "Advantage player1"
        else:
            return "Advantage player2"

    def combined_points_score(self):
        player1_result = get_score_name(self.player1_points)
        player2_result = get_score_name(self.player2_points)
        return player1_result + "-" + player2_result

    def equal_points_score(self):
        if self.player1_points == 0:
            return "Love-All"
        elif self.player1_points == 1:
            return "Fifteen-All"
        elif self.player1_points == 2:
            return "Thirty-All"
        else:
            return "Deuce"


def get_score_name(player_points):
    if player_points == 0:
        return "Love"
    elif player_points == 1:
        return "Fifteen"
    elif player_points == 2:
        return "Thirty"
    elif player_points == 3:
        return "Forty"
