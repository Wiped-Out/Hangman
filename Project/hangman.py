# Write your code here
from random import choice


class HangMan:

    def __init__(self):
        self.word: str = choice(('python', 'java', 'kotlin', 'javascript'))
        self.dashes: list = list("-" * len(self.word))
        self.counter: int = 1
        self.wrd_inp: set = set()

    def check_input(self, inp: str) -> bool:  # Checks if there's any errors
        if inp in self.wrd_inp:
            print('You already typed this letter')
            return False
        if 0 <= len(inp) > 1:
            print('You should print a single letter')
            return False
        if not inp.islower():
            print('It is not an ASCII lowercase letter')
            return False
        return True

    # Checks if letter is in word.
    def check_letter(self, letter: str) -> None:
        self.wrd_inp.add(letter)
        for n in range(len(self.word)):
            if self.word[n] == letter:
                self.dashes[n] = letter
        if letter not in set(self.word):
            self.counter += 1
            print('No such letter in the word')
            return

    def win_lose(self) -> None:
        if self.word == ''.join(self.dashes):
            print(f'You guessed the word {self.word}!')
            print('You survived!\n')
            self.menu()
        else:
            print('You are hanged!\n')
            self.menu()

    def menu(self) -> None:
        print('H A N G M A N')
        option = input('Type "play" to play the game, "exit" to quit: ')
        if option == 'play':
            self.game()
        else:
            exit()

    def game(self) -> None:
        while self.counter <= 8:
            print()
            print(''.join(self.dashes))
            usr_input: str = input('Input a letter: ')
            if self.check_input(usr_input) is False:
                continue
            else:
                self.check_letter(usr_input)
        self.win_lose()


HangMan().menu()
