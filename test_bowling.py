import unittest
from bowling import score


class BowlingScoreTest(unittest.TestCase):

    def test_no_strike_or_spare(self):
        result = '45 45 45 45 45 45 45 45 45 45'
        self.assertEqual(score(result), 90)

    def test__one_spare(self):
        result = '4/ 45 45'
        expected = (10+4) + 4+5 + 4+5
        self.assertEqual(score(result), expected)

    def test_multiple_spares(self):
        result = '4/ 5/ 12'
        expected = (10+5) + (10+1) + 1+2
        self.assertEqual(score(result), expected)

    def test_strikes(self):
        result = '11 XX 15 XX 22'
        expected = 1+1 + (10+1+5) + 1+5 + (10+2+2) + 2+2
        self.assertEqual(score(result), expected)

    def test_consecutive_strikes(self):
        result = 'XX XX 53'
        expected = (10+10+5) + (10+5+3) + 5+3
        self.assertEqual(score(result), expected)

    def test_consecutive_strikes_and_spare(self):
        result = 'XX XX 5/ 12 22'
        expected = (10+10+5) + (10+5+5) + (10+1) + 1+2 + 4
        self.assertEqual(score(result), expected)

    def test_3orMore_consecutive_strikes(self):
        result = 'XX XX XX 53'
        expected = (10+10+10) + (10+10+5) + (10+5+3) + 5+3
        self.assertEqual(score(result), expected)


if __name__ == "__main__":
    unittest.main()
