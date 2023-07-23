import random
import time
from collections import deque


#  -- initiate time pause --
def pause(a: float = 2.0) -> None:
    """
    Pause function to delay execution of next function
    :param a: float number for time is seconds to delay function
    """
    time.sleep(a)


#  -- roll dice when starting new round --
def roll_dice(players: deque) -> dict:
    """
    Rolling dice function that fill randomly generated dice for every player every round
    :param players: list of player objects for active players
    :return: dict with all of active players and their dice
    """
    players_turns = {}
    for player in players:
        player.clear_stat()
        player.clear_memory()
        player.clear_dice_stat_profile_for_opponents()
        if player.dice > 0:
            cells = []
            for cell in range(player.dice):
                dice_number = random.randint(1, 6)
                cells.append(dice_number)
            players_turns[player.name] = sorted(cells)
            player.load_stat(cells)
            player.load_initial_memory(cells)
    return players_turns


# -- print text according to game language --
def choose_language(english_language: bool, english: str, bulgarian: str) -> None:
    """
    Function that choose which parameter to display upon desired language from user
    :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
    :param english: string in english language
    :param bulgarian: string in bulgarian language
    """
    if english_language:
        print(english)
    else:
        print(bulgarian)
