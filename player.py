import random
from collections import deque


# -- player class to create both human and bot players --
class Player:
    game_players = deque()

    def __init__(self, player_name: str) -> None:
        self.turns = 1
        self.name = player_name
        self.dice = 5
        # according to temper bots place bluffs more or less often
        self.temper = random.uniform(0.25, 1)
        # here are dice in own hand
        self.stat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        # based on these stats opponents calculate temper of a player
        self.profile_for_opponents = {
            'tempers': 0,
            'total_calls': 0.01,
            'called_dice': [0, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}]
        }
        # if opponent is trustworthy player adds opponents' dice
        self.memory = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        # here is how opponent bots see temper of the player
        self.temper_for_other_players = 0

        Player.game_players.append(self)

    def restore_dice(self) -> None:
        self.dice = 5

    @staticmethod
    def restore_dice_players() -> None:
        [player.restore_dice() for player in Player.game_players]

    def clear_stat(self) -> None:
        self.stat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def clear_memory(self) -> None:
        self.memory = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def clear_dice_stat_profile_for_opponents(self) -> None:
        self.profile_for_opponents['called_dice'] = [0, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}]

    def calculate_temper_for_opponents(self) -> None:
        self.temper_for_other_players = self.profile_for_opponents['tempers'] / self.profile_for_opponents[
            'total_calls']

    # -- the sum of all dices on the table --
    @staticmethod
    def check_sum_dice() -> int:
        return sum([player.dice for player in Player.game_players])


class HumanPlayer(Player):
    def __init__(self, player_name: str) -> None:
        super().__init__(player_name)
