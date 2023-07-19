import random
from collections import deque

from pause import pause
from player import Player
from print import Print


# -- choosing number of bots and creates list of players with human player --
def create_list_of_players(number_of_bots: str, list_names_of_bots: list, game_players: deque, language: bool) -> None:
    list_of_bots = list_names_of_bots
    if number_of_bots.isdigit():
        if 0 < int(number_of_bots) <= len(list_of_bots):
            for j in range(int(number_of_bots)):
                c = list_of_bots[random.randint(0, len(list_names_of_bots) - 1)]
                list_of_bots.remove(c)
                Player(c)
        else:
            Print.text_incorrect_input_opponents(language, list_of_bots)
            create_list_of_players(input(), list_of_bots, game_players, language)
    else:

        Print.text_incorrect_input_opponents(language, list_names_of_bots)
        create_list_of_players(input(), list_names_of_bots, game_players, language)


# -- rotate players --
def next_turn(players: deque) -> None:
    players.append(players.popleft())

#
# #  -- get names of the players --
# def get_players_name(players: deque) -> list:
#     return [p.name for p in players]


# -- adds how many times player place a bet to self, helps to place bluffs according to temper --
def add_turn_to_player(player: Player) -> None:
    player.turns += 1


# -- show inactive player if any --
def players_active(players: deque, game_players_names: list, language: bool) -> list:
    active_players_names = game_players_names
    # players_names = []
    # inactive_names = []
    for player in players:
        if player.name in active_players_names:
            if player.dice == 0:
                Print.text_left_game(language, player)
                active_players_names.remove(player.name)

    return active_players_names


#  -- check which player lose a die
def check_who_lose_die(c_bidder: Player, l_bidder: Player, players_turns: dict, last_bet: list, g_players: deque,
                       g_players_names: list, wild: bool, language: bool) -> list:
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
        Print.text_result_and_who_lose_die(language, number_of_dices_of_searched_number, searched_number, l_bidder)
        remove_dice(l_bidder)
        g_players_names = players_active(g_players, g_players_names, language)
        choosing_player_to_start(l_bidder, g_players)
    else:
        Print.text_result_and_who_lose_die(language, number_of_dices_of_searched_number, searched_number, c_bidder)
        remove_dice(c_bidder)
        g_players_names = players_active(g_players, g_players_names, language)
        choosing_player_to_start(c_bidder, g_players)
    return g_players_names


#  -- choose player with dice to start round --
def choosing_player_to_start(player: Player, games_players: deque) -> None:
    while player != games_players[0]:
        next_turn(games_players)
        # to check if the following is needed
    if games_players[0].dice == 0:
        next_turn(games_players)


#  -- get the next bidder with dice from players --
def get_next_bidder(all_game_players: deque) -> Player:
    for i in range(len(all_game_players)):
        if all_game_players[i + 1].dice != 0:
            next_index = (i + 1) % len(all_game_players)
            return all_game_players[next_index]


#  -- check if there is a call from player and no such face dice in hand --
def check_if_players_are_bluffing(players: deque, wild: bool) -> None:
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


#  -- when someone is challenged show dice in players hand --
def print_if_liar(current_player: Player, last_player: Player, player_turn: dict, language: bool) -> None:
    Print.text_someone_call_other_liar(language, current_player, last_player)
    showing_string = ''
    for pln, d in player_turn.items():
        showing_string += pln
        word = Print.get_verb(language)
        showing_string += str(word)
        showing_string += ', '.join(map(str, d))
        showing_string += ' ; '
    print(f'{showing_string[:-2]}')
    pause()


#  -- remove dice from player --
def remove_dice(loser: Player):
    if loser.dice > 0:
        loser.dice -= 1


# -- action if someone is called a liar --
def if_liar(current_bidder: Player, last_bidder: Player, players_turn, english_language, old_bet, game_players,
            players_names, wild_mode):
    print_if_liar(current_bidder, last_bidder, players_turn, english_language)
    players_names = check_who_lose_die(current_bidder, last_bidder, players_turn, old_bet, game_players, players_names,
                                       wild_mode, english_language)

    check_if_players_are_bluffing(game_players, wild_mode)
    check_who_is_liar = True
    return [players_names, check_who_is_liar]
