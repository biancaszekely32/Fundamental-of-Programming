from repository.repo import RepoError
from validation.validators import ValidError


class Game:
    def __init__(self, service):
        self.service = service
        self.sentence = self.service.choose_a_sentence().strip()
        self.hangman_output = ""
        self.output_sentence = self.initial_output_sentence().strip()
        self.hangman = "hangman"

    def start_game(self):
        print("STARTING THE GAME: ")
        print(self.output_sentence)
        while True:
            _continue = self.game_round()
            if _continue == 1 or _continue == 0:
                return

    def initial_output_sentence(self):
        split = self.sentence.split(" ")
        output_sentence = ""
        for word in split:
            word.strip()

            for i in range(0, len(word)):
                if i == 0 or i == len(word) - 1:
                    output_sentence += word[i]
                else:
                    output_sentence += "_"
            output_sentence += " "
        return output_sentence

    def choose_a_letter(self):
        while True:
            letter = input("pick a letter")
            if len(letter) == 1 and letter.isalpha() is True:
                return letter
            print("choose a valid letter")

    def output_with_letter(self):
        letter = self.choose_a_letter()
        if letter in self.sentence:
            self.reveal_letters_output(letter)
        else:
            index = len(self.hangman_output)
            print(index)
            print(self.hangman[index])
            self.hangman_output += self.hangman[index]

    def reveal_letters_output(self, letter):
        conversion = ""
        for i in range(0, len(self.sentence)):
            if self.sentence[i] == letter:
                conversion += letter
            else:
                conversion += self.output_sentence[i]
                print(self.output_sentence[i])
        self.output_sentence = conversion

    def game_round(self):
        self.output_with_letter()
        print("sentence:")
        print(self.output_sentence)
        if self.output_sentence == self.sentence:
            print("YOU WON")
            return 1
        elif self.hangman == self.hangman_output:
            print("YOU LOST")
            return 0
        else:
            print("current hangman:")
            print(self.hangman_output)


class UI:
    def __init__(self, service, repo):
        self.service = service
        self.repo = repo

    def boot_up(self):
        print("WELCOME TO HANGMAN")
        print()
        while True:
            print("options: ")
            print("1. add a sentence")
            print("2. play game")
            print("3. exit")
            user_choice = input("choose an option: ").strip()
            try:
                if user_choice == "1":
                    self.add_a_sentence()
                elif user_choice == "2":
                    self.start_game()
                elif user_choice == "3":
                    return
                else:
                    print("unavailable option")
            except ValidError as ve:
                print(str(ve))
            except RepoError as re:
                print(str(re))

    def add_a_sentence(self):
        sentence = input("Add a sentence: ").strip()
        split_sentence = sentence.split(" ")
        new_sentence = ""
        for word in split_sentence:
            word = word.strip()
            new_sentence = new_sentence + word + " "
        self.service.add_a_sentence(new_sentence)

    def start_game(self):
        game = Game(self.service)
        game.start_game()
