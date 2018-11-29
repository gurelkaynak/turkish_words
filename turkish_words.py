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
        while max_try_count > 0:
            max_try_count -= 1
            choice = random.choice(self.initial_letters)
            if choice not in exclude_letters:
                return choice
        return None

    def random_word(self):
        return random.choice(self.turkish_words[self.random_initial_letter()])

    def random_word_with_initial(self, initial: str):
        return random.choice(self.turkish_words[initial])

    def random_word_excluding_initials(self, exclude_letters: list):
        max_try_count = len(self.initial_letters)
        while max_try_count > 0:
            max_try_count -= 1
            choice = random.choice(self.initial_letters)
            if choice not in exclude_letters:
                return self.turkish_words[choice]
        return None
