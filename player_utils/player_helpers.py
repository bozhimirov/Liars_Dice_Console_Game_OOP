import random
from collections import deque
from utils.betting_helpers import place_bet, calc_bet_according_to_temper, bluff_bet
from player_utils.player import Player
from utils.output import Output
from utils.validators import Validators


# -- choosing number of bots and creates list of players with human player --
def create_list_of_players(number_of_bots: str, list_names_of_bots: list, language: bool) -> None:
    """
    Creates list of players according to chosen number of bots
    :param number_of_bots: string from player input that points to chosen number of bots in the game
    :param list_names_of_bots: list with predefined bots names
    :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    """
    list_of_bots = list_names_of_bots
    if number_of_bots.isdigit():
        if 0 < int(number_of_bots) <= len(list_of_bots):
            for j in range(int(number_of_bots)):
                c = list_of_bots[random.randint(0, len(list_names_of_bots) - 1)]
                list_of_bots.remove(c)
                Player(c)
        else:
            Output.text_incorrect_input_opponents(language, list_of_bots)
            create_list_of_players(input(), list_of_bots, language)
    else:

        Output.text_incorrect_input_opponents(language, list_names_of_bots)
        create_list_of_players(input(), list_names_of_bots, language)


# -- rotate players --
def next_turn(players: deque) -> None:
    """
    Rotates players so on the first index to be the next player in turn
    :param players: list with players objects in the game
    """
    players.append(players.popleft())


# -- show inactive player if any --
def players_active(players: deque, game_players_names: list, language: bool) -> list:
    """

    :param players: list with players objects in the game
    :param game_players_names: list with names of players
    :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :return: list with names of active players
    """
    active_players_names = game_players_names
    for player in players:
        if player.name in active_players_names:
            if player.dice == 0:
                Output.text_left_game(language, player)
                active_players_names.remove(player.name)

    return active_players_names


#  -- check which player lose a die
def check_who_lose_die(c_bidder: Player, l_bidder: Player, players_turns: dict, last_bet: list, g_players: deque,
                       g_players_names: list, wild: bool, language: bool) -> list:
    """
    check which player lose a die, current player or last player according to last bet and dice in players' hands
    :param c_bidder: player object for current bidder
    :param l_bidder: player object for last bidder
    :param players_turns: dict with dice of players
    :param last_bet: list with values of last bet
    :param g_players: list with player objects
    :param g_players_names: list with names of players
    :param wild: bool value that indicates the game mode
    :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :return: list with names of active players
    """
    searched_number = int(last_bet[1])
    number_of_dices_of_searched_number = 0
    for k, v in players_turns.items():
        for i in range(len(v)):
            if wild:
                if v[i] == searched_number or v[i] == 1:
                    number_of_dices_of_searched_number += 1
            else:
                if v[i] == searched_number:
                    number_of_dices_of_searched_number += 1
    if number_of_dices_of_searched_number < int(last_bet[0]):
        Output.text_result_and_who_lose_die(language, number_of_dices_of_searched_number, searched_number, l_bidder)
        l_bidder.dice -= 1
        g_players_names = players_active(g_players, g_players_names, language)
        choosing_player_to_start(l_bidder, g_players)
    else:
        Output.text_result_and_who_lose_die(language, number_of_dices_of_searched_number, searched_number, c_bidder)
        c_bidder.dice -= 1
        g_players_names = players_active(g_players, g_players_names, language)
        choosing_player_to_start(c_bidder, g_players)
    return g_players_names


#  -- choose player with dice to start round --
def choosing_player_to_start(player: Player, games_players: deque) -> None:
    """
    choosing player to start the game from active players list
    :param player: player object for player to start the game
    :param games_players: list with player objects
    """
    while player != games_players[0]:
        next_turn(games_players)
        # to check if the following is needed
    if games_players[0].dice == 0:
        next_turn(games_players)


#  -- get the next bidder with dice from players --
def get_next_bidder(all_game_players: deque) -> Player:
    """
    find next active player from list of player objects
    :param all_game_players: list of player objects
    :return: player object that is next bidder
    """
    for i in range(len(all_game_players)):
        if all_game_players[i + 1].dice != 0:
            next_index = (i + 1) % len(all_game_players)
            return all_game_players[next_index]


#  -- check if there is a call from player and no such face dice in hand --
def check_if_players_are_bluffing(players: deque, wild: bool) -> None:
    """
    check if players are bluffing according to their bets and dive values in their hands
    :param players: list of player objects
    :param wild: bool value that indicates the game mode
    """
    for player in players:
        bluffer = 0
        if player.profile_for_opponents['called_dice'][0] != 0:
            for i in range(1, 7):
                if wild:
                    if (player.profile_for_opponents['called_dice'][1][i] > 0) and (
                            (player.stat[i] == 0) or (player.stat[1] == 0)):
                        bluffer += 1
                else:
                    if (player.profile_for_opponents['called_dice'][1][i] > 0) and (player.stat[i] == 0):
                        bluffer += 1
            if bluffer > 0 and player.dice != 0:
                player.profile_for_opponents['tempers'] += 0
                player.profile_for_opponents['total_calls'] += 1
            elif bluffer <= 0 and player.dice != 0:
                player.profile_for_opponents['tempers'] += 1
                player.profile_for_opponents['total_calls'] += 1
        player.calculate_temper_for_opponents()


# -- action if someone is called a liar --
def if_liar(current_bidder: Player, last_bidder: Player, players_turn, english_language, old_bet, game_players,
            players_names, wild_mode) -> list:
    """
    when someone is called liar, check who loose a die and check if players are bluffing
    :param current_bidder: player object for current bidder
    :param last_bidder: player object for last bidder
    :param players_turn: dict with dice of players
    :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :param old_bet: list with values of last bet
    :param game_players: list with player objects
    :param players_names: list with names of players
    :param wild_mode: bool value that indicates the game mode
    :return: list with list of players' names and bool value if someone is called liar
    """
    Output.print_if_liar(current_bidder, last_bidder, players_turn, english_language)
    players_names = check_who_lose_die(current_bidder, last_bidder, players_turn, old_bet, game_players, players_names,
                                       wild_mode, english_language)

    check_if_players_are_bluffing(game_players, wild_mode)
    check_who_is_liar = True
    return [players_names, check_who_is_liar]


def if_player_human(current_bidder, english_language, sum_dice, players_turn, last_bidder, old_bet) -> list:
    """
    If player is human makes action according to chosen input
    :param current_bidder: player object for current bidder
    :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :param sum_dice: number of dice on the table
    :param players_turn: dict with dice of players
    :param last_bidder: player object for last bidder
    :param old_bet: list with values of last bet
    :return: liar statement and last bet
    """
    old_bet = old_bet
    Output.text_your_turn_and_info(english_language, sum_dice, players_turn,
                                   Player.human_player.name)
    if old_bet == [sum_dice, 6]:
        liar = True
        return [liar, old_bet]
    elif len(last_bidder) > 0:
        Output.text_if_there_is_last_bidder(english_language, last_bidder)

        action = Validators.validate_input_action(input(), english_language)

        if action == 'bet':
            Output.text_place_bet(english_language)
            new_human_bet = Validators.validate_if_bet_is_valid(english_language, old_bet, sum_dice)
            return place_bet(new_human_bet, current_bidder, english_language)

        else:
            liar = True
            return [liar, old_bet]
    else:
        Output.text_place_bet(english_language)
        new_human_bet = Validators.validate_if_bet_is_valid(english_language, old_bet, sum_dice)
        return place_bet(new_human_bet, current_bidder, english_language)


def if_player_bot(old_bet, current_bidder, last_bidder, sum_dice, wild_mode) -> tuple:
    """
    If player is bot makes action according to last bidder or last bet
    :param old_bet: list with values of last bet
    :param current_bidder: player object for current bidder
    :param last_bidder: player object for last bidder
    :param sum_dice: number of dice on the table
    :param wild_mode: bool value that indicates the game mode
    :return: tuple with list of values of the new bet and the next bidder
    """
    new_bet = calc_bet_according_to_temper(old_bet, current_bidder, last_bidder, sum_dice, wild_mode)
    next_bidder = get_next_bidder(Player.game_players)
    if new_bet:
        if last_bidder == '':
            while int(new_bet[0]) > (sum_dice - next_bidder.dice):
                new_bet_to_be_checked_again = bluff_bet(old_bet, sum_dice, current_bidder, last_bidder, wild_mode,
                                                        0)
                new_bet = new_bet_to_be_checked_again
        else:
            if int(new_bet[0]) > (sum_dice - next_bidder.dice):
                new_bet = []
    return new_bet, next_bidder
