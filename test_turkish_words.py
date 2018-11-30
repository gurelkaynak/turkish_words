import random
import unittest
from turkish_words import TurkishWords


class TestTurkishWords(unittest.TestCase):
    """
    https://softwareengineering.stackexchange.com/questions/147134/how-should-i-test-randomness
    """
    initial_letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö',
                       'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    test_safe_initials = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                          'u', 'v', 'y', 'z']

    def setUp(self):
        self.turkish_words = TurkishWords()

    def test_random_word_excluding_all_initials(self):
        self.assertRaises(AssertionError,
                          self.turkish_words.random_word_excluding_initials, self.turkish_words.initial_letters)

    def test_random_word_excluding_random_initials(self):
        for i in range(0, 1000):
            exclude_letters = random.sample(self.turkish_words.initial_letters,
                                            random.randint(0, len(self.turkish_words.initial_letters)-1))
            for j in range(0, 100):
                word_initial = self.turkish_words.random_word_excluding_initials(exclude_letters=exclude_letters)
                self.assertNotIn(word_initial, exclude_letters)

    def test_initial_letters(self):
        self.assertEqual(self.initial_letters, self.turkish_words.initial_letters)

    def _test_words_under_letter(self, letter):
        for word in self.turkish_words.turkish_words[letter]:
            self.assertEqual(letter, word[0].lower())

    def test_word_data(self):
        for letter in self.test_safe_initials:
            self.assertIn(letter, self.turkish_words.turkish_words)
            self._test_words_under_letter(letter)

    def test_random_initial_letter(self):
        for i in range(0, 10000):
            letter = self.turkish_words.random_initial_letter()
            self.assertIsInstance(letter, str)

    def test_random_word(self):
        for i in range(0, 10000):
            letter = self.turkish_words.random_word()
            self.assertIsInstance(letter, str)

    def test_random_initial_letters_excluding_all(self):
        self.assertRaises(
            AssertionError,
            self.turkish_words.random_initial_excluding, **{'exclude_letters': self.turkish_words.initial_letters})

    def test_random_word_with_random_safe_initials(self):
        for i in range(0, 100000):
            random_initial = random.choice(self.test_safe_initials)
            random_word_with_random_initial = self.turkish_words.random_word_with_initial(random_initial)

            self.assertEqual(random_initial, random_word_with_random_initial[0].lower())

    def test_random_word_with_wrong_initial(self):
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, 'ab')
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, '.')
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, 'x')
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, ';')
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, '!')
        self.assertRaises(AssertionError, self.turkish_words.random_word_with_initial, '"')


if __name__ == '__main__':
    unittest.main()
