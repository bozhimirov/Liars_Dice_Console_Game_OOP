import unittest

from utils.validators import Validators


class InputTest(unittest.TestCase):
    def setUp(self):
        self.previous_bet = [3, 4]
        self.sum_dice = 12

    def test_correct_bet(self):
        current_bet = [5, 6]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = True
        self.assertEqual(result, expected_result)

    def test_blank_bet(self):
        current_bet = []
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_less_num(self):
        current_bet = [2, 4]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_less_num_and_value(self):
        current_bet = [2, 1]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_less_num_and_more_value(self):
        current_bet = [2, 5]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = True
        self.assertEqual(result, expected_result)

    def test_bet_with_less_value_and_more_num(self):
        current_bet = [5, 2]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_more_dice_than_all(self):
        current_bet = [13, 5]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_zero_dice_number(self):
        current_bet = [0, 5]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_zeroes(self):
        current_bet = [0, 0]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_zero_value(self):
        current_bet = [5, 0]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_same_value(self):
        current_bet = [3, 4]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_string_value(self):
        current_bet = ['3', '4']
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_one_value(self):
        current_bet = [3]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_bet_with_more_than_2_values(self):
        current_bet = [3, 4, 5]
        result = Validators.valid_bet(current_bet, self.previous_bet, self.sum_dice)
        expected_result = False
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
