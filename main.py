import random

from utils.betting_helpers import place_bet
from utils.helper_functions import roll_dice, pause
from utils.list_of_opponents import list_names_of_bots
from player_utils.player import Player, HumanPlayer
from player_utils.player_helpers import create_list_of_players, choosing_player_to_start, next_turn, if_liar, if_player_human, \
    if_player_bot
from utils.validators import Validators
from utils.output import Output


class Game(Validators, Output):
    def __init__(self) -> None:
        self.english_language = True
        self.wild_mode = False
        self.active_game = True
        self.last_bidder = ''
        self.check_who_is_liar = False
        self.old_bet = ['0', '0']
        self.players_turn = {}
        self.game_round = 0
        self.liar = False
        self.players_names = []

    def language(self) -> bool:
        self.text_choose_language()
        english_language = self.validate_language(input().strip())
        return english_language

    def create_human_player(self, player_input_name: str) -> None:
        human_player_name = self.validate_name(player_input_name.strip(), self.english_language, list_names_of_bots)
        Player.human_player = HumanPlayer(human_player_name)
        pause(0.5)

    def create_opponents(self, player_input_bots: str) -> None:
        create_list_of_players(player_input_bots.strip(), list_names_of_bots, Player.game_players,
                               self.english_language)
        pause(0.5)

    def choose_mode(self, player_input_mode: str) -> None:
        self.wild_mode = self.validate_game_mode(player_input_mode.strip(), self.english_language)
        pause(0.5)

    def choose_end(self, player_input_end: str) -> None:
        self.active_game = self.validate_input_answer(player_input_end.strip(), self.english_language)
        pause()

    def new_game(self) -> None:

        self.players_turn = {}
        self.game_round = 0

        while self.active_game:
            self.players_names = Player.take_names_of_players()
            self.text_tell_len_players(self.english_language, self.players_names)
            self.text_choosing_player(self.english_language)
            index_of_player_index = random.randint(0, len(Player.game_players) - 1)
            starter_player = Player.game_players[index_of_player_index]
            choosing_player_to_start(starter_player, Player.game_players)
            self.text_who_starts_the_game(self.english_language, Player.game_players)
            Player.restore_dice_players()

            self.new_round()

            self.text_tell_winner(self.english_language, self.players_names)
            self.text_new_game_option(self.english_language)
            self.choose_end(input())

    def new_round(self) -> None:

        while len(self.players_names) > 1:
            self.game_round += 1
            self.liar = False
            self.new_roll()
            self.while_not_liar()

    def new_roll(self) -> None:

        sum_dice = Player.check_sum_dice()
        self.players_turn = roll_dice(Player.game_players, self.game_round)
        self.line()
        self.text_new_round_number(self.english_language, self.game_round, self.players_names, sum_dice)
        self.check_who_is_liar = False
        self.last_bidder = ''
        self.old_bet = ['0', '0']

    def human_bet(self, player_input_bet: str) -> str:
        action = self.validate_input_action(player_input_bet.strip(), self.english_language)
        pause(0.5)
        return action

    def while_not_liar(self) -> None:
        while not self.check_who_is_liar:
            sum_dice = Player.check_sum_dice()
            while Player.game_players[0].name not in self.players_names:
                next_turn(Player.game_players)
            current_bidder = Player.game_players[0]
            if current_bidder == Player.human_player:
                [self.liar, self.old_bet] = if_player_human(current_bidder, self.english_language, sum_dice,
                                                            self.players_turn, self.last_bidder, self.old_bet)
                pause()
            else:
                [new_bet, next_bidder] = if_player_bot(self.old_bet, current_bidder, self.last_bidder, sum_dice,
                                                       self.wild_mode)

                if len(new_bet) == 0:
                    [self.players_names, self.check_who_is_liar] = if_liar(current_bidder, self.last_bidder,
                                                                           self.players_turn, self.english_language,
                                                                           self.old_bet, Player.game_players,
                                                                           self.players_names, self.wild_mode)
                    break
                elif self.old_bet == [sum_dice, 6]:
                    self.liar = True
                elif new_bet[0] > (sum_dice - next_bidder.dice) and self.last_bidder != '':
                    self.liar = True
                else:
                    [self.liar, self.old_bet] = place_bet(new_bet, current_bidder, self.english_language)

            if self.liar:
                [self.players_names, self.check_who_is_liar] = if_liar(current_bidder, self.last_bidder,
                                                                       self.players_turn, self.english_language,
                                                                       self.old_bet, Player.game_players,
                                                                       self.players_names, self.wild_mode)
                break
            self.last_bidder = current_bidder
            next_turn(Player.game_players)
            pause()
            self.check_who_is_liar = False

    def run(self) -> None:
        self.text_choose_name(self.english_language)
        self.create_human_player(input())
        self.text_choose_opponents(self.english_language)
        self.create_opponents(input())
        self.text_choose_mode(self.english_language)
        self.choose_mode(input())
        self.new_game()


if __name__ == "__main__":
    game = Game()
    game.english_language = game.language()
    game.run()
