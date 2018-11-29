import random
import unittest
from turkish_words import TurkishWords


class TestTurkishWords(unittest.TestCase):
    def setUp(self):
        self.turkish_words = TurkishWords()

    def test_random_word_excluding_initials(self):
        self.assertIsNone(self.turkish_words.random_word_excluding_initials(self.turkish_words.initial_letters))

        for i in range(0, 100):
            exclude_letters = random.sample(self.turkish_words.initial_letters,
                                            random.randint(0, len(self.turkish_words.initial_letters)-1))
            for j in range(0, 100):
                word_initial = self.turkish_words.random_word_excluding_initials(exclude_letters=exclude_letters)
                self.assertNotIn(word_initial, exclude_letters)

    def test_initials(self):
        initial_letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö',
                           'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
        self.assertEqual(initial_letters, self.turkish_words.initial_letters)

    def test_random_word_with_initial(self):
        for i in range(0, 1000):
            random_initial = self.turkish_words.random_initial_letter()
            random_word_with_random_initial = self.turkish_words.random_word_with_initial(random_initial)

            self.assertEqual(random_initial, random_word_with_random_initial[0])


if __name__ == '__main__':
    unittest.main()
