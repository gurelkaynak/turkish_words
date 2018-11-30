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

    def random_initial_letter(self) -> str:
        return random.choice(self.initial_letters)

    def random_initial_excluding(self, exclude_letters: list) -> str:
        available_letter_choices: list = list(filter(lambda x: x not in exclude_letters, self.initial_letters))
        assert len(available_letter_choices) > 0

        return random.choice(available_letter_choices)

    def random_word(self) -> str:
        return random.choice(self.turkish_words[self.random_initial_letter()])

    def random_word_with_initial(self, initial: str) -> str:
        assert initial in self.initial_letters

        return random.choice(self.turkish_words[initial])

    def random_word_excluding_initials(self, exclude_letters: list) -> str:
        try:
            return self.turkish_words[self.random_initial_excluding(exclude_letters=exclude_letters)]
        except KeyError:
            return None
