import random
import time
from collections import deque


#  -- initiate time pause --
def pause(a: float = 2.0) -> None:
    time.sleep(a)


#  -- roll dice when starting new round --
def roll_dice(players: deque, g_round: int) -> dict:
    g_round += 1
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
    if english_language:
        print(english)
    else:
        print(bulgarian)
