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
    ## guessing
        if (self.winner == "tie"):
            print("Tie game!")
        elif (self.winner == 'X' or self.winner == 'O'):
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
    # OPTIONAL
    # Call upon print_board
    ## Call upon print_message
        self.print_board()
        self.print_message()




# creating a game, then calling the play game method.
game_instance = Game()
game_instance.play_game()
game_instance.render()
