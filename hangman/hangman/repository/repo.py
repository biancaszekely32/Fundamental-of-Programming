class RepoError(Exception):
    pass


class Repository:
    def __init__(self, file_name):
        self._sentences = list()
        self._file_name = file_name
        self.load_file()

    def __len__(self):
        return len(self._sentences)

    def get_all_sentences(self):
        return self._sentences

    def save_file(self):
        """saves all the sentences in the file"""
        f = open(self._file_name, "wt")
        sentences = self.get_all_sentences()
        for sentence in sentences:
            f.write(sentence.strip()+'\n')
        f.close()

    def load_file(self):
        """gets all the sentences from the file"""
        f = open(self._file_name, "rt")
        for line in f.readlines():
            if line != '\n':
                self._sentences.append(line)
        f.close()

    def add_sentence(self, sentence):
        """adds a sentence to the file and repo"""
        self._sentences.append(sentence)
        self.save_file()

    def get_sentence(self, i):
        """gets a sentence from the index i"""
        return self._sentences[i]

