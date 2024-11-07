class Game():
    def __init__(self,):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
                        'a1': None, 'b1': None, 'c1': None,
                        'a2': None, 'b2': None, 'c2': None,
                        'a3': None, 'b3': None, 'c3': None,
                    }
    
    def play_game(self):
        print("ITS TIME TO PLAY THE GAMEEEEEE")

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
    ## If there is a tie: print("Tie game!")
    ## If there is a winner: print(f"{self.winner} wins the game!")
    ## Otherwise: print(f"It's player {self.turn}'s turn!")
        if (self.winner == "tie"):
            print("Tie game!")
        elif (self.winner == 'X' or self.winner == 'O'):
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
    # OPTIONAL
        self.print_board()
        self.print_message()
        self.get_move()
        self.switch_turn()
        self.winner_check()

    
    def get_move(self):
        while True:
            move = input(f"Enter a valid movie (example: A1): ").lower()
            if self.board.get(move):
                # Check if self.board is occupied
                print('invalid move, space is occupied')
            elif move in self.board:
                self.board[move] = self.turn
                self.print_board()
                break
            else:
                # move does not exist in self.board
                print('Invalid move. Please enter a valid movie (example: A1): ')
        # print(move)
        # prompt user for input
        # If the input is valid, update the board and break the loop
        # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
    
    def winner_check(self): 
        # TEST THIS OH GOD IM JUST COPYING CODE FROM THE JS VERSION
        winning_combinations = [
            ['a1', 'b1', 'c1'], #toprow
            ['a2', 'b2', 'c2'], #middlerow
            ['a3', 'b3', 'c3'], #bottomrow
            ['a1', 'a2', 'a3'], #leftcolumn
            ['b1', 'b2', 'b3'], #middlecolumn
            ['c1', 'c2', 'c3'], #rightcolumn
            ['a1', 'b2', 'c3'], #diagonal from top left to bottom right
            ['c1', 'b2', 'a3'], #diagnol from top right to bottom left
        ]
        for combo in winning_combinations:
            # unsure if I'm writing this correctly, in JS:
            if (self.board[combo[0]]):
                if(self.board[combo[0]] == self.board[combo[1]]):
                    if (self.board[combo[0]] == self.board[combo[2]]):
                        self.winner = self.turn
                        print(f"WE HAVE A WINNER: {self.winner}")

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"
        print(self.turn)


# creating a game, then calling the play game method.
game_instance = Game()
game_instance.play_game()
# game_instance.render()
game_instance.switch_turn()
game_instance.switch_turn()

