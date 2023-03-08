class ValidError(Exception):
    pass


class Validate_Sentence:
    def __init__(self, sentence):
        self.sentence = sentence.strip()

    def check_validity(self):
        """
        checks whether the words in the sentence are too short
        if the sentence is valid, the function returns True
        """
        split = self.sentence.split(" ")
        for word in split:
            word = word.strip()
            if len(word) < 3:
                raise ValidError("words are too short")
        return True
