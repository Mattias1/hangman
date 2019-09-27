#
#  Hangman
# =========
#     _______
#    |/     |
#    |      O
#    |     /|)
#    |     / )
# __/|\_________
#
# A small game of hangman on the command line
#
import sys


class Hangman:
    MAX_MISTAKES = 10

    def __init__(self, word='test'):
        self.word = word.upper()
        self.guesses = []
        self.mistakes = 0

    def play(self):
        self.draw_intro()

        while True:
            try:
                guesses = input('\nGuess a letter: \n> ').upper()

                self.guess(guesses)
                self.draw()

                if self.has_ended():
                    msg = 'Game over!' if self.has_lost() else 'Congratulations!'
                    input('\n{} Hit enter to exit...\n> '.format(msg))
                    return

            except KeyboardInterrupt:
                print(' Bye!')
                return

    def guess(self, guesses):
        for c in guesses:
            if c in self.guesses:
                continue
            self.guesses.append(c)
            if not c in self.word:
                self.mistakes += 1
            if self.has_ended():
                return

    def has_lost(self):
        return self.mistakes >= self.MAX_MISTAKES

    def has_won(self):
        for c in self.word:
            if not c in self.guesses:
                return False
        return True

    def has_ended(self):
        return self.has_lost() or self.has_won()

    def draw(self):
        self.draw_intro()
        self.draw_gallow()
        self.draw_letters()

    def draw_intro(self):
        print()
        print('  Hangman')
        print(' =========')
        # print(' Press Ctrl+C to exit')

    def draw_gallow(self):
        pic = [[' '] * 15 for _ in range(6)]

        if self.mistakes > 0:
            pic[5][1:14] = '_____________'
        if self.mistakes > 1:
            pic[4][4] = '.'
            pic[5][3:5] = '/_\\'
        if self.mistakes > 2:
            for i in range(1, 6):
                pic[i][4] = '|'
        if self.mistakes > 3:
            for i in range(5, 12):
                pic[0][i] = '_'
        if self.mistakes > 4:
            pic[1][5] = '/'
        if self.mistakes > 5:
            pic[1][11] = '|'
        if self.mistakes > 6:
            pic[2][11] = 'O'
        if self.mistakes > 7:
            pic[3][11] = '|'
        if self.mistakes > 8:
            pic[3][10:12] = '/|)'
        if self.mistakes > 9:
            pic[4][10:12] = '/ )'

        if self.has_lost():
            pic[2][14] = '  GAME OVER :('
        if self.has_won():
            pic[2][14] = '  CONGRATULATIONS (:'

        print('\n'.join([''.join(line) for line in pic]))

    def draw_letters(self):
        letters = [c if c in self.guesses else '_' for c in self.word]
        print('\n {}\n\n History: {} ({}/{})'.format(
            ' '.join(letters),
            ', '.join(self.guesses),
            self.mistakes,
            self.MAX_MISTAKES))
        # A comment to prevent the formatter from screwing up

def main():
    args = sys.argv[1:]
    try:
        word = args[0]
    except:
        word = 'test'

    game = Hangman(word)
    game.play()

main()
