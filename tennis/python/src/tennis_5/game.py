class Game:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_score = 0
        self.player_2_score = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.player_1_score += 1
        elif player_name == self.player_2_name:
            self.player_2_score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        match (self.player_1_score, self.player_2_score):
            case (p1, p2) if p1 < 4 and p2 < 4:
                return self._match_early_game()
            case (p1, p2) if p1 == p2 and p1 > 3:
                return "Deuce"
            case (p1, p2) if p1 - p2 == 1 and p1 > 3:
                return f"Advantage {self.player_1_name}"
            case (p1, p2) if p2 - p1 == 1 and p2 > 3:
                return f"Advantage {self.player_2_name}"
            case (p1, p2) if p1 - p2 > 1 and p1 > 3:
                return f"Win for {self.player_1_name}"
            case (p1, p2) if p2 - p1 > 1 and p2 > 3:
                return f"Win for {self.player_2_name}"

    def _match_early_game(self):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        match (self.player_1_score, self.player_2_score):
            case (p1, p2) if p1 != p2:
                return f"{score_names[p1]}-{score_names[p2]}"
            case (p1, p2) if p1 == p2 and p1 < 3:
                return f"{score_names[p1]}-All"
            case (p1, p2) if p1 == p2:
                return "Deuce"
