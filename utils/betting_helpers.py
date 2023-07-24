import random

from player_utils.player import Player
from utils.output import Output
from probability_calculation import calculate_probability
from utils.validators import Validators


# --calculate test new  bet --
def calculate_new_bet(last_bet: list, player: Player, last_player: Player, sum_of_dice: int, wild: bool,
                      opponents_chance: float) -> list:
    """
    Calculates new bet according to memory and dice in hand
    :param last_bet: list of values for last bet
    :param player: current player object for current bidder
    :param last_player: player object for last bidder
    :param sum_of_dice: number of dice on the table
    :param wild: bool value that indicates the game mode
    :param opponents_chance: float number from 0 to 1 that indicates the probability of placed bet to be valid when
     number close to 1 is
        with very high probability
    :return: list of values for new bet
    """
    if last_player != '':
        neo_bet = []

        if 0 < last_player.temper_for_other_players < 0.55:
            if player.temper < 0.55:
                if 0 < opponents_chance < 0.7:
                    neo_bet = []
                    return neo_bet
            else:
                if 0 < opponents_chance < 0.5:
                    neo_bet = []
                    return neo_bet

        else:
            sum_dice_in_memory, probability_by_memory, new_test_bet = if_not_blank_bet(
                player, last_bet, opponents_chance, sum_of_dice, wild, last_player)

            if sum_dice_in_memory < sum_of_dice and probability_by_memory > 0.6:
                neo_bet = new_test_bet
            elif opponents_chance != 0:
                neo_bet = []
            else:
                neo_bet = bluff_bet(last_bet, sum_of_dice, player, last_player, wild, opponents_chance)

        if opponents_chance > 0.9 and neo_bet == []:
            neo_bet = bluff_bet(last_bet, sum_of_dice, player, last_player, wild, opponents_chance)
        if player.temper < 0.55:
            coefficient = 0.2
            if wild:
                coefficient = 0.3

            if int(last_bet[0]) != 0 and int(last_bet[0]) > sum_of_dice * coefficient:
                return []
        else:
            coefficient = 0.3
            if wild:
                coefficient = 0.45
            if int(last_bet[0]) != 0 and int(last_bet[0]) > sum_of_dice * coefficient:
                return []
        return neo_bet
    else:
        sum_dice_in_memory, probability_by_memory, new_test_bet = if_not_blank_bet(
            player, last_bet, opponents_chance, sum_of_dice, wild, last_player)
        return new_test_bet


#  -- if the new bet is not blank(call previous player liar) --
def if_not_blank_bet(player: Player, last_bet: list, opponents_chance: float, sum_of_dice: int, wild: bool,
                     last_player: Player) -> list:
    """
    Calculates new bet according to memory and dice in hand
    :param player: current player object for current bidder
    :param last_bet: list of values for last bet
    :param opponents_chance: float number from 0 to 1 that indicates the probability of placed bet to be valid when
     number close to 1 is
        with very high probability
    :param sum_of_dice: number of dice on the table
    :param wild: bool value that indicates the game mode
    :param last_player: player object for last bidder
    :return: list with sum of dice, probability for win with last bet and new bet
    """
    prev_count, prev_dice = last_bet
    prev_count = int(prev_count)
    prev_dice = int(prev_dice)
    new_test_bet = []
    sum_dice_in_memory = sum(player.memory.values())
    for k, v in player.memory.items():
        if wild:
            if (v > prev_count and k == prev_dice) or (1 <= v <= sum_of_dice and k > prev_dice):
                if (v - prev_count) >= 0 or (player.memory[1] - prev_count) >= 0:
                    v = prev_count + 1
                if Validators.valid_bet([v, k], last_bet, sum_of_dice):
                    new_test_bet = [v, k]
                    break
        else:
            if (v > prev_count and k == prev_dice) or (1 <= v <= sum_of_dice and k > prev_dice):
                if (v - prev_count) >= 0:
                    v = prev_count + 1
                if Validators.valid_bet([v, k], last_bet, sum_of_dice):
                    new_test_bet = [v, k]
                    break

    probability_by_memory = calculate_probability(last_bet, sum_of_dice, player, wild, 'memory')
    if opponents_chance > 0.6 and len(new_test_bet) == 0:
        new_test_bet = bluff_bet(last_bet, sum_of_dice, player, last_player, wild, opponents_chance)
    return [sum_dice_in_memory, probability_by_memory, new_test_bet]


# -- place bet on table --
def place_bet(current_bet: list, player: Player, language: bool) -> list:
    """
    Player place a new bet on the table and saves stats in memory
    :param current_bet: list of values for current bet
    :param player: current player object
    :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :return: list with liar statement and list with dice values for previous bet
    """
    player.load_memory(current_bet)
    player.turns += 1
    Output.text_player_bet(language, player, current_bet)
    previous_bet = current_bet
    liar_statement = False
    return [liar_statement, previous_bet]


#  -- according to temper and times player places bet in the round, choose if the bet is bluff or not --
def calc_bet_according_to_temper(last_bet: list, current_player: Player, last_player: Player, sum_of_dice: int,
                                 wild: bool) -> list:
    """
    Returns bet according to temper, if temper is more like a liar - bet is a bluff bet, else it is bet according to
        dice in hand
    :param last_bet: list of values for last bet
    :param current_player: player object for current bidder
    :param last_player: player object for last bidder
    :param sum_of_dice: number of dice on the table
    :param wild: bool value that indicates the game mode
    :return: list with values of new bet
    """
    new_bet_to_be_checked = []
    opponents_chance = 0

    if current_player.temper <= 0.35:
        if current_player.turns % 3 == 0:
            new_bet_to_be_checked = calculate_new_bet(
                last_bet, current_player, last_player, sum_of_dice, wild, opponents_chance)
        else:
            new_bet_to_be_checked = bluff_bet(
                last_bet, sum_of_dice, current_player, last_player, wild, opponents_chance)
    elif 0.35 < current_player.temper <= 0.55:
        if current_player.turns % 2 == 0:
            new_bet_to_be_checked = calculate_new_bet(
                last_bet, current_player, last_player, sum_of_dice, wild, opponents_chance)
        else:
            new_bet_to_be_checked = bluff_bet(
                last_bet, sum_of_dice, current_player, last_player, wild, opponents_chance)
    elif 0.55 < current_player.temper <= 0.75:
        if current_player.turns % 3 == 0:
            new_bet_to_be_checked = bluff_bet(
                last_bet, sum_of_dice, current_player, last_player, wild, opponents_chance)
        else:
            new_bet_to_be_checked = calculate_new_bet(
                last_bet, current_player, last_player, sum_of_dice, wild, opponents_chance)
    elif current_player.temper > 0.75:
        if current_player.turns % 4 == 0:
            new_bet_to_be_checked = bluff_bet(
                last_bet, sum_of_dice, current_player, last_player, wild, opponents_chance)
        else:
            new_bet_to_be_checked = calculate_new_bet(
                last_bet, current_player, last_player, sum_of_dice, wild, opponents_chance)
    # --- returning empty bet equal to calling liar ---
    if int(last_bet[0]) >= sum_of_dice:
        new_bet_to_be_checked = []
    elif int(last_bet[1]) != 0:
        if wild:
            if int(last_bet[0]) > \
                    (sum_of_dice - current_player.dice) + current_player.stat[int(last_bet[1])] + \
                    current_player.stat[1]:
                new_bet_to_be_checked = []
        else:
            if int(last_bet[0]) > \
                    (sum_of_dice - current_player.dice) + current_player.stat[int(last_bet[1])]:
                new_bet_to_be_checked = []

    return new_bet_to_be_checked


#  -- calculate bluff bet --
def dice_modifier(prev_dice: int, wild: bool) -> list:
    """
    Modifies dice values according to game mode
    :param prev_dice: int with face value of die
    :param wild: bool value that indicates the game mode
    :return: list with previous die value and new die value
    """
    if prev_dice == 6:
        new_dice = 6
    elif prev_dice == 0:
        if wild:
            prev_dice = 1
            new_dice = 2
        else:
            new_dice = 1
    else:
        new_dice = prev_dice + 1

    return [prev_dice, new_dice]


def bluff_bet(prev_bet: list, sum_of_dice: int, current_player: Player, last_player: Player, wild: bool,
              opponents_chance: float) -> list:
    """
    Makes bluff bet according to mode and previous conditions
    :param prev_bet: list of values for last bet
    :param sum_of_dice: number of dice on the table
    :param current_player: player object for current bidder
    :param last_player: player object for last bidder
    :param wild: bool value that indicates the game mode
    :param opponents_chance: float number from 0 to 1 that indicates the probability of placed bet to be valid when
     number close to 1 is
        with very high probability
    :return: list with values of new bet
    """
    if last_player != '':
        new_bet_to_be_checked = []
        if wild:
            if int(prev_bet[0]) > \
                    sum_of_dice - current_player.memory[int(prev_bet[1])] - current_player.memory[1] - last_player.dice:
                new_bet_to_be_checked = []
        else:
            if int(prev_bet[0]) > sum_of_dice - current_player.memory[int(prev_bet[1])] - last_player.dice:
                new_bet_to_be_checked = []
        coefficient = 0.15
        if wild:
            coefficient = 0.25
        if int(prev_bet[0]) > sum_of_dice * coefficient:
            new_bet_to_be_checked = []
        if opponents_chance > 0.9 and new_bet_to_be_checked == []:
            prev_count, prev_dice = prev_bet
            prev_dice = int(prev_dice)
            prev_count = int(prev_count)
            for i in range(900):
                new_count = 0
                new_dice = 0
                rand_num = random.randint(0, 1)
                if rand_num == 0:
                    if wild:
                        rand_count = random.randint(1, 2)
                        new_count = prev_count + rand_count
                    else:
                        new_count = prev_count + 1
                    new_dice = prev_dice
                    if prev_dice == 0:
                        if wild:
                            new_dice = 2
                        else:
                            new_dice = 1
                else:
                    for index in range(sum_of_dice):
                        new_count = random.randint((index + 1), (index + 2))
                        dice_modifier(prev_dice, wild)
                        new_bet_to_be_checked = [new_count, new_dice]
                        valid_condition = Validators.valid_bet(new_bet_to_be_checked, prev_bet, sum_of_dice)
                        if valid_condition:
                            break
                new_bet_to_be_checked = [new_count, new_dice]
                valid_condition = Validators.valid_bet(new_bet_to_be_checked, prev_bet, sum_of_dice)
                if valid_condition:
                    return new_bet_to_be_checked
            return new_bet_to_be_checked
    prev_count, prev_dice = prev_bet
    prev_dice = int(prev_dice)
    prev_count = int(prev_count)
    for i in range(900):
        new_count = 0
        new_dice = 0
        rand_num = random.randint(0, 1)
        if rand_num == 0:
            new_count = prev_count + random.randint(1, 2)
            new_dice = prev_dice
            if prev_dice == 0:
                if wild:
                    new_dice = 2
                else:
                    new_dice = 1
        else:
            for index in range(1, sum_of_dice):
                if prev_count < 5:
                    new_count = random.randint(index, (index + 2))
                else:
                    new_count = random.randint(index, (index + 1))
                dice_modifier(prev_dice, wild)
                if prev_dice == 6:
                    new_dice = 6
                elif prev_dice == 0:
                    if wild:
                        prev_dice = 1
                        new_dice = 2
                    else:
                        new_dice = 1
                else:
                    new_dice = prev_dice + 1
                new_bet_to_be_checked = [new_count, new_dice]
                valid_condition = Validators.valid_bet(new_bet_to_be_checked, prev_bet, sum_of_dice)
                if valid_condition:
                    break
        new_bet_to_be_checked = [new_count, new_dice]
        valid_condition = Validators.valid_bet(new_bet_to_be_checked, prev_bet, sum_of_dice)
        if valid_condition:
            return new_bet_to_be_checked
    return []
