import sys
import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        cur_guess = input(f'Guess a number between {START} and {END}: ')

        if not cur_guess:
            raise ValueError('Please enter a number')

        try:
            cur_guess = int(cur_guess)
        except ValueError:
            raise ValueError('Should be a number')

        if cur_guess in self._guesses:
            raise ValueError('Already guessed')
        elif cur_guess < START or cur_guess > END:
            print(f'cur_guess = {cur_guess}', file=sys.stderr, flush=True)
            raise ValueError('Number not in range')

        self._guesses.add(cur_guess)

        return cur_guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        correct = False
        if guess > self._answer:
            print(f'{guess} is too high')
        elif guess < self._answer:
            print(f'{guess} is too low')
        else:
            print(f'{guess} is correct!')
            correct = True
            self._win = True

        return correct

    def __repr__(self):
        rep = f'''_guesses = {self._guesses}
        _win = {self._win}
        _answer = {self._answer}
        '''
        return rep

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""

        while len(self._guesses) < MAX_GUESSES:
            try:
                if self._validate_guess(self.guess()):
                    print(f'It took you {len(self._guesses)} guesses')
                    break
            except ValueError as e:
                print(e)
                continue
        else:
             print(f'Guessed {len(self._guesses)} times, answer was {self._answer}')



if __name__ == '__main__':
    game = Game()
    game()
