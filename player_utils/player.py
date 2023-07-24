import random
from collections import deque


# -- player class to create both human and bot players --
class Player:
    """
    A Player class that makes a player for game
    """
    # -- filled immediately after initialization --
    game_players = deque()
    human_player = None
    game_players_names = []

    def __init__(self, player_name: str) -> None:
        """
        constructor that initialize player's name, count player's turns, add 5 dice to player, calculate player's temper
        /according to temper player is more or less liar/, stores player's dice for every round, saves opponents profile
        saves memory for dice played, adds player object to game_players and name of player in game_players_names
        :param player_name: string with name of the player
        """
        # # -- how many times player place a bet, helps to place bluffs according to temper --
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
        Player.game_players_names.append(self.name)

    def __len__(self) -> int:
        """
        Calculate length of name of the player
        :return: integer with length of name of player
        """
        return len(self.name)

    # -- if player want to know how bots are rating their temper from 0 - liar to 1 - trustworthy --
    # -- not implemented --
    def get_temper(self) -> float:
        """
        Takes temper from player object and return it
        :return: float number displaying temper of the player
        """
        return self.temper_for_other_players

    # -- restore initial count of dice in player hand --
    def restore_dice(self) -> None:
        """
        restore initial count of dice in player's hand. makes dice equal to five
        """
        self.dice = 5

    # -- restore initial count of dice in every players' hand --
    @staticmethod
    def restore_dice_players() -> None:
        """
        restore initial count of dice for each player. makes dice for every player equal to five
        """
        [player.restore_dice() for player in Player.game_players]

    # -- clear stat for dice in player --
    def clear_stat(self) -> None:
        """
        clear stat for dice in player memory
        """
        self.stat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    #  -- load dice values when new round starts --
    def load_stat(self, data: list) -> None:
        """
        add dice values to memory of player
        :param data: list with dice values
        """
        for i in range(len(data)):
            self.stat[data[i]] += 1

    # -- clear dice values in player memory--
    def clear_memory(self) -> None:
        """
        clear saved dice values in memory of player
        """
        self.memory = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    #  -- load self dices to memory --
    def load_initial_memory(self, data: list) -> None:
        """
        saves dice value for each player in player's memory
        :param data:
        """
        for i in range(len(data)):
            self.memory[data[i]] += 1

    #  -- load other players bets to memory if their stat is trustworthy--
    def load_memory(self, bet: list) -> None:
        """
        saves bets values to player's memory
        :param bet: list of bet's values
        """
        for player in Player.game_players:
            if self != player and self.temper_for_other_players > 0.55:
                player.memory[int(bet[1])] += 1
            elif self == player and player.dice != 0:
                player.profile_for_opponents['called_dice'][0] += 1
                player.profile_for_opponents['called_dice'][1][int(bet[1])] += 1

    # -- clear dice stat for opponents --
    def clear_dice_stat_profile_for_opponents(self) -> None:
        """
        clear saved dice for opponents profile in player
        """
        self.profile_for_opponents['called_dice'] = [0, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}]

    # -- calculate temper for opponents --
    def calculate_temper_for_opponents(self) -> None:
        """calculate temper for opponents based on their bets and the dice in their hand"""
        self.temper_for_other_players = self.profile_for_opponents['tempers'] / self.profile_for_opponents[
            'total_calls']

    # -- the sum of all dices on the table --
    @staticmethod
    def check_sum_dice() -> int:
        """
        calculate sum of dice in all players' hand
        :return: integer with sum of all dice on table
        """
        return sum([player.dice for player in Player.game_players])

    # -- names of the players --
    @staticmethod
    def take_names_of_players() -> list:
        """
        takes player objects for current game and add their names to game_player_names
        :return: list with names of players in current game
        """
        Player.game_players_names = [player.name for player in Player.game_players]
        return Player.game_players_names


class HumanPlayer(Player):
    """
    A Human Player class that extends Player class and make human player for the game
    """
    def __init__(self, player_name: str) -> None:
        """
        constructor that initialize player's name, count player's turns, add 5 dice to player, calculate player's temper
        /according to temper player is more or less liar/, stores player's dice for every round, saves opponents profile
        saves memory for dice played, adds player object to game_players and name of player in game_players_names and
        also adds player object to human_player
        :param player_name: string with name of the player
        """
        super().__init__(player_name)
        Player.human_player = self
