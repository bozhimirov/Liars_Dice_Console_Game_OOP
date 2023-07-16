import random
from collections import deque

from stats_memory_players import load_stat, load_initial_memory


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
            load_stat(player, cells)
            load_initial_memory(player, cells)
    return players_turns


# -- the sum of all dices on the table --
def check_sum_dice(players: deque) -> int:
    return sum([player.dice for player in players])


# -- print text according to game language --
def choose_language(english_language: bool, english: str, bulgarian: str) -> None:
    if english_language:
        print(english)
    else:
        print(bulgarian)


# -- function to print text on console asking for game language--

def text_choose_language() -> None:
    print("Choose language/Избери език")
    print("Please type 'e' for English or/или напишете 'b' за Български")


# -- print ask for valid language choice --

def text_valid_language() -> None:
    print("Please make your choice by pressing 'e' or 'b' button on your keyboard!")
    print("Моля натиснете 'e' или 'b' бутона на клавиатурата!")
    print("By pressing 'е' you will play the game in English. By pressing 'b' you will play the game in Bulgarian.")
    print("Натискайки 'e' ще играете играта на английски език. Натискайки 'b' ще играете играта на български език.")
