import random

class RPSPlayer:

    moves = ['rock','paper','scissors']

    def __init__(self, score=0, user_score=0):
        self.score = score
        self.user_score = user_score

    def move(self, user_move):
        if user_move in self.moves:
            comp_move = random.choice(self.moves)
            print('Computer move: '+comp_move)
            if user_move == comp_move:
                print('Draw')
            elif (user_move == 'rock' and comp_move == 'paper') or (user_move == 'paper' and comp_move == 'scissors') or (user_move == 'scissors' and comp_move == 'rock'):
                self.score += 1
                print('I win!')
            else:
                self.user_score += 1
                print('You win!')
        else:
            print('Play your move by typing \'Rock\', \'Paper\', or \'Scissors\'')

    def start_game(self):
        print('\nRock-Paper-Scissors\n')
        print('The outcome of the game is determined by 3 simple rules:\n* Rock wins against scissors.\n* Scissors win against paper.\n* Paper wins against rock.\n')
        print('Type your move when prompted. Type Q to quit.')
        while True:
            user_move = input('Your turn: ').strip().lower()
            if user_move == 'q':
                self.end_game()
                break
            else:
                self.move(user_move)

    def end_game(self):
        print('\nComputer score: %s' %self.score)
        print('Your score: %s' %self.user_score)

# start playing
RPSPlayer().start_game()
