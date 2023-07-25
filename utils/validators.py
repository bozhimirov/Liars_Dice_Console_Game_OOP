from utils.helper_functions import return_text
from utils.output import Output
import re


class Validators:

    # -- choose human action - bet or liar --
    @staticmethod
    def validate_input_action(string: str, language: bool) -> str:
        """
        Validate player input for choosing from two options - bet/'b'/ or liar/'l'/ with pressing keyboard keys
        :param string: player's input on console
        :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language.
        :return: string with validated input action
        """
        text_action = return_text(language, 'Your choice: ', 'Вашият избор: ')
        if string.lower() == 'b':
            return 'bet'
        elif string.lower() == 'l':
            return 'liar'
        else:
            Output.text_valid_action_again(language)
            new_human_string = input(text_action).strip()
            human_action = Validators.validate_input_action(new_human_string, language)
            return human_action

    # -- validate name of human player / cannot be blank / --
    @staticmethod
    def validate_name(name: str, language: bool, list_of_bots: list) -> str:
        """
        Validate player input for choosing username
        :param name: player's input on console
        :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
        :param list_of_bots: list of names of all bot players already predefined
        :return: string with validated input name
        """
        text_name = return_text(language, 'Username: ', 'Име: ')
        if name in list_of_bots:
            Output.text_choose_name_again(language)
            new_human_name = input(text_name).strip()
            new_name = Validators.validate_name(new_human_name, language, list_of_bots)
            return new_name
        elif len(name) < 2 or type(name) != str or name[0].isnumeric() or not re.match('^[A-Za-z0-9_]*$', name):
            Output.text_name_len_more_than_two(language)
            new_human_name = input(text_name).strip()
            new_name = Validators.validate_name(new_human_name, language, list_of_bots)
            return new_name
        return name

    # -- check answer if human wants to play again with the same players--
    @staticmethod
    def validate_input_answer(human_answer: str, language: bool) -> bool:
        """
        Validate player input for choosing from two options - yes/'y'/ or no/'n'/ with pressing keyboard keys
        :param human_answer: player's input on console as string
        :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
        :return: bool that indicates if user wants to continue with another game
        """
        text_answer = return_text(language, 'Your choice: ', 'Вашият избор: ')
        if human_answer.lower() == 'y':
            game_active = True
            return game_active
        elif human_answer.lower() == 'n':
            game_active = False
            return game_active
        else:
            Output.text_make_valid_choice(language)
            new_human_answer = input(text_answer).strip()
            new_game_active = Validators.validate_input_answer(new_human_answer, language)
            return new_game_active

    #  -- human choice for game mode regular/normal or advanced/wild ones --
    @staticmethod
    def validate_game_mode(human_answer: str, language: bool) -> bool:
        """
        Validate player input for choosing from two options - wild/'w'/ or normal/'n'/ with pressing keyboard keys
        :param human_answer: player's input on console as string
        :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
        :return: bool that indicates game mode chosen by user
        """
        text_mode = return_text(language, 'Your choice: ', 'Вашият избор: ')
        if human_answer.lower() == 'w':
            w_mode = True
            return w_mode
        elif human_answer.lower() == 'n':
            w_mode = False
            return w_mode
        else:
            Output.text_choose_valid_mode(language)
            new_human_answer = input(text_mode).strip()
            new_w_mode = Validators.validate_input_answer(new_human_answer, language)
            return new_w_mode

    @staticmethod
    def validate_if_bet_is_valid(language: bool, old_bet: list, sum_dice: int) -> list:
        """
        Validate if the current bet is valid
        :param language: bool variable showing the choice of the user for language of communication
                According to that variable user receives instructions on desired language
        :param old_bet: list of old bet in format [count of dice] [face of die]
        :param sum_dice: number of dice on the table
        :return: list of valid bet in format [count of dice] [face of die]
        """
        text_bet = return_text(language, 'Your bet: ', 'Вашият залог: ')
        valid_human_bet = False
        new_human_bet = []
        while not valid_human_bet:
            new_human_bet = input(text_bet).strip() \
                .split(' ')
            valid_human_bet = Validators.valid_bet(new_human_bet, old_bet, sum_dice)
            if not valid_human_bet:
                Output.text_valid_bet_again(language)
        return new_human_bet

    # -- validate bets --
    @staticmethod
    def valid_bet(current_bet: list, previous_bet: list, sum_of_dice: int) -> bool:
        """
        Validate if bet is valid, have to be a list with 2 numbers and the new bet have rise the old bet
        :param current_bet: list of current bet in format [count of dice] [face of die]
        :param previous_bet: list of old bet in format [count of dice] [face of die]
        :param sum_of_dice: number of dice on the table
        :return: bool value if bet is valid
        """
        if len(current_bet) != 2:
            return False
        elif not (str(current_bet[0]).isdigit() and str(current_bet[1]).isdigit()):
            return False
        else:
            if previous_bet == ['0', '0']:
                if (1 <= int(current_bet[0]) <= sum_of_dice) and (1 <= int(current_bet[1]) <= 6):
                    return True
                else:
                    return False
            else:
                if (sum_of_dice >= int(current_bet[0]) > int(previous_bet[0]) and (
                        int(previous_bet[1]) == int(current_bet[1]))) \
                        or ((1 <= int(current_bet[0]) <= sum_of_dice) and int(current_bet[1]) > int(previous_bet[1])):
                    if int(current_bet[1]) > 6:
                        return False
                    return True
                else:
                    return False

    #  -- human choice for language preferences --
    @staticmethod
    def validate_language(human_answer: str) -> bool:
        """
        Validate player input for choosing from two options - english/'e'/ or bulgarian/'b'/ with pressing keyboard keys
        :param human_answer: player's input on console as string
        :return: bool value for choosing language, true for english and false for bulgarian
        """
        if human_answer.lower() == 'e':
            return True
        elif human_answer.lower() == 'b':
            return False
        else:
            Output.text_valid_language()
            new_human_answer = input("Your choice/Твоят избор: ").strip()
            language = Validators.validate_language(new_human_answer)
            return language
