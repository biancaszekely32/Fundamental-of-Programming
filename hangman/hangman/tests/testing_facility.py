import unittest
from repository.repo import Repository, RepoError

class Test_Repo(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository("tests.txt")
        self.sentence_add = "ana are mere"

    def test_add_sentence(self):
        self.repo.add_sentence(self.sentence_add)
        self.repo.get_sentence(0) == self.sentence_add