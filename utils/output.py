from utils.helper_functions import choose_language, pause
from collections import deque

from player_utils.player import Player


class Output:

    # -- function to print text on console asking for game language--
    @classmethod
    def text_choose_language(cls) -> None:
        """
        Prints question for user to choose a language.
        Print available typing options / 'e' or 'b'/ for the user that a will asure that the game will continue.
        'e' stands for English language while 'b' stands for Bulgarian language.
        """
        print("Choose language/Избери език")
        print("Please type 'e' for English or/или напишете 'b' за Български")

    # -- print ask for valid language choice --
    @classmethod
    def text_valid_language(cls) -> None:
        """
        Print available typing options / 'e' or 'b'/ to ensure that the game will continue.
        'e' stands for English language while 'b' stands for Bulgarian language.
        Explains what will happen if user choose either of options.
        """
        print("Please make your choice by pressing 'e' or 'b' button on your keyboard!")
        print("Моля натиснете 'e' или 'b' бутона на клавиатурата!")
        print("By pressing 'е' you will play the game in English. By pressing 'b' you will play the game in Bulgarian.")
        print("Натискайки 'e' ще играете играта на английски език. Натискайки 'b' ще играете играта на български език.")

    # -- function to print text on console asking for player's name--
    @staticmethod
    def text_choose_name(english_language: bool) -> None:
        """
        Print question asking the user about the chosen username
        :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, "What is your name?", "Какво е вашето име?")

    # -- print asks for choice --
    @staticmethod
    def ask_for_choice(english_language: bool) -> None:
        """
        Print question about what is the choice of the user
        :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, 'What is your choice?', 'Какъв е твоят избор?')

    # -- function to print text on console asking for number of opponents--
    @staticmethod
    def text_choose_opponents(english_language: bool) -> None:
        """
        Print prompt for the user to choose number of the opponents for the game
        :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, "Choose number of opponents.", "Изберете броя на противниците си.")

    # -- function to print text on console asking for game mode--
    @staticmethod
    def text_choose_mode(english_language: bool) -> None:
        """
        Print prompt for choosing game mode.
        Print available choosing options / 'n' or 'w'/.
        'n' stands for standard game, while 'w' stands for "wild one's mode"
        :param english_language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language,
                        "Choose gaming mode. Please type 'n' for regular game, or type 'w' for accessing "
                        "wild one's mode.", "Изберете ниво на трудност. Моля напишете 'n' за обикновена "
                                            "игра или напишете 'w' за да влезете в режим 'луди единици'.")

    # -- function to print text on console telling choosing player to start--
    @staticmethod
    def text_choosing_player(english_language: bool) -> None:
        """
        Print statement than game choose who to start the game
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, 'Choosing player to start the game.',
                        'Избира се играч, който да започне играта.')
        pause()

    # -- prints line with num len --
    @staticmethod
    def line(num: int = 60) -> None:
        """
        Print a line on the console from repeating the symbol '-'
        :param num: number of repetition of the symbol '-'.
        """
        print(f'{num * "-"}')

    # -- print text asking valid bet --
    @staticmethod
    def text_place_bet(english_language: bool) -> None:
        """
        Print question about what is the choice of the user
        Print statement with instructions how user to place correct bet
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        Output.ask_for_choice(english_language)
        choose_language(english_language,
                        'Place your bet in format [count of dice] [face of die] separated by space.',
                        'Направи залог във формат [брой зарове] [стойност на зара] разделени с интервал.')

    # -- print aks for a new game --
    @staticmethod
    def text_new_game_option(english_language: bool) -> None:
        """
        Print question if user want to play again a game with the same players.
        Print choices for user 'y' for yes and 'n' for no
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, 'Do you like to start again?', 'Искаш ли да играеш отново?')
        print(
            '[y/n]'
        )

    # --  print asks for valid action again --
    @staticmethod
    def text_valid_action_again(english_language: bool) -> None:
        """
        Print statement than user have to make a valid choice
        Print available choosing options / 'b' or 'l'/
        'b' stands for bet statement, while 'l' stands for liar statement
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, "Please make a valid choice! Type 'b' or 'l'. ",
                        "Моля направете валиден избор! Напишете 'b' или 'l'. ")

    # -- print asks for length more than 2 symbols --
    @staticmethod
    def text_name_len_more_than_two(english_language: bool) -> None:
        """
        Print statement with instructions about requirements for valid username
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, "Please write a name longer than 2 symbols(numbers and letters)"
                                          " and start with a letter!",
                        "Моля напишете име с дължина повече от 2 символа(букви и цифри), започващо с буква!")

    # -- print ask for valid choice --
    @staticmethod
    def text_make_valid_choice(english_language: bool) -> None:
        """
        Print statement about valid choices for user
        'y' stands for yes and 'n' stands for no
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language,
                        "Please make your choice by pressing 'y' or 'n' button on your keyboard!",
                        "Моля направете избор като натиснете 'y' или 'n' бутона на клавиатурата си!")

    # -- print ask for valid mode --
    @staticmethod
    def text_choose_valid_mode(english_language: bool) -> None:
        """
        Print statement prompting user to make a valid choice by suggesting options from keyboard.
        Print explanations what will happen if user press both options.
        By pressing 'w' user will enter "wild one's mode", by pressing 'n' user will enter standard game
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language,
                        "Please make your choice by pressing 'w' or 'n' button on your keyboard!",
                        "Моля направете своя избор като натиснете 'w' или 'n' бутона на клавиатурата си!")
        choose_language(english_language,
                        "By pressing 'w' you will enter advanced wild one's mode. By pressing 'n' you will "
                        "play a regular game.", "Натискайки 'w' ще задействате режима на лудите единици. "
                                                "Натискайки 'n' ще играете обикновена игра.")

    # -- print ask for valid bet again --
    @staticmethod
    def text_valid_bet_again(english_language: bool) -> None:
        """
        Print prompt for user to place a valid bet.
        Print instructions about how user to place a bet in correct format.
        Print instructions about how user to place a bet in correct type to ensure that bet will be valid
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, 'Please place a valid bet! Place bet in format: [count of dice] [face of die]'
                                          'separated by space. You should rise the last bid and type only numbers!',
                        'Моля направете валиден залог! Напишете залог във формат: [брой зарове] [стойност на зара] '
                        'разделени с интервал. Трябва да вдигнете последният залог и да пишете само с цифри!')

    # -- print ask for new name --
    @staticmethod
    def text_choose_name_again(english_language: bool) -> None:
        """
        Print statement that chosen username is already taken and prompts user to choose another username
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        choose_language(english_language, "Name taken, please choose another username.", "Името е заето, моля изберете "
                                                                                         "друго име.")

    # -- print ask for new number of opponents --
    @staticmethod
    def text_incorrect_input_opponents(english_language: bool, list_names_of_bots: list) -> None:
        """
        Print statement that user made incorrect input.
        Print instructions about a valid number of opponents and the interval that user have to choose from
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param list_names_of_bots: list with all the bots' names
        """
        choose_language(english_language,
                        f"Incorrect input. Please type just one number for opponents between 1 and"
                        f" {len(list_names_of_bots)}.",
                        f"Грешна стойност. Моля напишете само едно число за брой противници в интервала от 1 до"
                        f" {len(list_names_of_bots)}.")

    # -- get verb according to language --
    @staticmethod
    def get_verb(english_language: bool) -> str:
        """
        Return a word according to desired language that has to be concatenated with other words from another function
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language.
        """
        if english_language:
            return ' has '
        else:
            return ' има '

    # -- function to print text on console telling number of active players--
    @staticmethod
    def text_tell_len_players(english_language: bool, players_names: list) -> None:
        """
        Print the number of the active players on the table and their names
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param players_names: list of names of all players playing the game.
        """
        choose_language(english_language,
                        f"There are {len(players_names)} players on the table - {', '.join(players_names)} ",
                        f"Има {len(players_names)} играчи на масата - {', '.join(players_names)} ")
        pause()

    # -- function to print text on console telling who starts the game--
    @staticmethod
    def text_who_starts_the_game(english_language: bool, game_players: deque) -> None:
        """
        Print which player will start the game
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param game_players: players as objects from all the active players listed
        """
        choose_language(english_language, f'{game_players[0].name} starts the game.', f'{game_players[0].name} '
                                                                                      f'започва играта.')
        pause()

    # -- print new round text and players with dice--
    @staticmethod
    def text_new_round_number(english_language: bool, game_round: int, players_names: list, sum_dice: int) -> None:
        """
        Print how many players are playing in the current round and the sum of the dice on the table
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param game_round: number of the current round of the current game
        :param players_names: list of names of all players playing the game
        :param sum_dice: number of dice on the table
        """
        choose_language(english_language, f'Starting round {game_round}.', f'Започва рунд {game_round}.')
        bg_word = 'зар' if sum_dice == 1 else 'зара'
        choose_language(english_language,
                        f'There are {len(players_names)} players with total {sum_dice} dice on the'
                        ' table.', f'Има {len(players_names)} играчи с общо {sum_dice} {bg_word} на масата.')
        pause()

    # -- print it is your turn and tell info about total dice and own dice--
    @staticmethod
    def text_your_turn_and_info(english_language: bool, sum_dice: int, players_turn: dict, human_player: str) -> None:
        """
        Print statement that it's user's turn
        Print the number of dice on the table for the current round
        Print your dice face value
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param sum_dice: number of dice on the table
        :param players_turn: dict with current dice for each active player
        :param human_player: name of the human player
        """

        choose_language(english_language, "It's your turn now!", "Твой ред е!")
        pause(1)
        choose_language(english_language, f"There are {sum_dice} dice on the table.",
                        f"Има {sum_dice} зарa на масата.")
        pause(1)
        choose_language(english_language, f"You have in your hand: {players_turn[human_player]}.",
                        f"В ръката си имаш: {players_turn[human_player]}.")
        pause()

    # -- print text if there is a last winner with options for bet or call liar--
    @staticmethod
    def text_if_there_is_last_bidder(english_language: bool, last_bidder: Player) -> None:
        """
        Print question about what is the choice of the user
        Print statement prompting user to make a choice and gives user options to choose from.
        'b' stands for bet, 'l' stands for calling last bidder liar
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param last_bidder: player object that last made a bet.
        """
        Output.ask_for_choice(english_language)
        choose_language(english_language, f"Place a bet [b] or call {last_bidder.name} a liar [l].",
                        f"Направи залог [b] или наречи {last_bidder.name} лъжец [l].")

    # -- print announcement of winner and congrats --
    @staticmethod
    def text_tell_winner(english_language: bool, players_names: list) -> None:
        """
        Print the name of the winner
        Print congrats
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param players_names: list of names of all players playing the game.
        """
        choose_language(english_language, f'The winner is {players_names[0]}.',
                        f'Победителят е {players_names[0]}.')
        choose_language(english_language, 'Congratulations!', 'Поздравления!')
        pause()

    # -- print the bet of the player --
    @staticmethod
    def text_player_bet(english_language: bool, player: Player, current_bet: list) -> None:
        """
        Print name of the player and his bet
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param player: player object for current player
        :param current_bet: list of values for current player bet for number of dice and face value of dice.
        """
        bg_word = 'зар' if current_bet[0] == 1 else 'зара'
        choose_language(english_language,
                        f'{player.name} bet for at least {current_bet[0]} dice with face number'
                        f' {current_bet[1]}.',
                        f'{player.name} залага за най-малко {current_bet[0]} {bg_word} със стойност'
                        f' {current_bet[1]}.')
        pause()

    # -- print who left the game --
    @staticmethod
    def text_left_game(english_language: bool, inactive_name: Player) -> None:
        """
        Print name of the player that left the game
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param inactive_name: player object that has left the game.
        """
        choose_language(english_language, f'Player {inactive_name.name} left the game.',
                        f'Играч {inactive_name.name} напусна играта.')
        pause()

    # -- print result and who lost a die --
    @staticmethod
    def text_result_and_who_lose_die(english_language: bool, number_of_dice_of_searched_value: int,
                                     searched_number: int, l_bidder: Player) -> None:
        """
        Print number of dice of searched value and searched value
        Print the name of the player that loses a die
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param number_of_dice_of_searched_value: number of dice of searched face value
        :param searched_number: number of searched face value of dice
        :param l_bidder: player object that last made a bet
        """
        choose_language(english_language,
                        f'There are {number_of_dice_of_searched_value} numbers of {searched_number} dices.'
                        f' {l_bidder.name} '
                        f'lose a dice.',
                        f'Има {number_of_dice_of_searched_value} броя зара със стойност {searched_number}'
                        f'. {l_bidder.name} губи зарче.')
        pause()

    # -- print someone call other liar --
    @staticmethod
    def text_someone_call_other_liar(english_language: bool, current_player: Player, last_player: Player) -> None:
        """
        Print the name of the player that call someone a liar and the name of the player that is called liar
        Print statement that everybody have to show their dice
        :param english_language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        :param current_player: player object that made the current bet
        :param last_player: player object that last made a bet
        """
        choose_language(english_language, f'{current_player.name} called {last_player.name} a liar.'
                                          f' Everyone showing their dice.',
                        f'{current_player.name} нарече {last_player.name} лъжец. Всички играчи показват заровете си.')
        pause()

    #  -- when someone is challenged show dice in players hand --
    @staticmethod
    def print_if_liar(current_player: Player, last_player: Player, player_turn: dict, language: bool) -> None:
        """
        Print the name of the player that call someone a liar and the name of the player that is called liar
        Print statement that everybody have to show their dice
        Print all players' names and the values of their dice
        :param current_player: player object that made the current bet
        :param last_player: player object that last made a bet
        :param player_turn: dict with current dice for each active player
        :param language: bool variable showing the choice of the user for language of communication.
                According to that variable user receives instructions on desired language
        """
        Output.text_someone_call_other_liar(language, current_player, last_player)
        showing_string = ''
        for pln, d in player_turn.items():
            showing_string += pln
            word = Output.get_verb(language)
            showing_string += str(word)
            showing_string += ', '.join(map(str, d))
            showing_string += ' ; '
        print(f'{showing_string[:-2]}')
        pause()
