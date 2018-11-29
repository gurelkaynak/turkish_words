import json
import gzip
import random


class TurkishWords(object):
    turkish_words: dict
    initial_letters: list

    def __init__(self):
        with gzip.open("turkish_words.json.gz", "rb") as file:
            self.turkish_words = json.loads(file.read())
            self.initial_letters = list(self.turkish_words.keys())

    def random_initial_letter(self):
        return random.choice(self.initial_letters)

    def random_initial_excluding(self, exclude_letters: list):
        max_try_count = len(self.initial_letters)
        for i in range(0, max_try_count):
            choice = self.random_initial_letter()
            if choice not in exclude_letters:
                return choice
        return None

    def random_word(self):
        return random.choice(self.turkish_words[self.random_initial_letter()])

    def random_word_with_initial(self, initial: str):
        return random.choice(self.turkish_words[initial])

    def random_word_excluding_initials(self, exclude_letters: list):
        try:
            return self.turkish_words[self.random_initial_excluding(exclude_letters=exclude_letters)]
        except KeyError:
            return None
