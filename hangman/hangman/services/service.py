"""service class"""
import random

from repository.repo import Repository, RepoError
from validation.validators import Validate_Sentence
from random import randint


class Service:
    def __init__(self, repo):
        self._repo = repo

    def add_a_sentence(self, sentence):
        """adds a sentence to the file,
        first the sentence is validated
        then it is checked to be unique
        finally added into the repo/file"""
        sentence = sentence.strip()
        valid = Validate_Sentence(sentence)
        if valid.check_validity() is True:
            """check its uniqueness"""
            sentences = self._repo.get_all_sentences()
            for sentence_from_repo in sentences:
                if sentence_from_repo.strip() == sentence:
                    raise RepoError("non-unique sentence")
            self._repo.add_sentence(sentence)

    def choose_a_sentence(self):
        """
        used to choose a sentence randomly from the file.
        :return:
        """
        upper_limit = len(self._repo)-1
        lower_limit = 0
        choice = random.randint(lower_limit, upper_limit)
        return self._repo.get_sentence(choice)



