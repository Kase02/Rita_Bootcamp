import random

class LudoGame:
    def __init__(self):
        self.board = [0] * 52
        self.players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
        self.piece_positions = {player: [0] * 4 for player in self.players}
        self.current_player_index = 0
        self.dice_rolls = []

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.dice_rolls.append(roll)
        return roll

    def move_piece(self, piece_index, spaces):
        player = self.players[self.current_player_index]
        current_position = self.piece_positions[player][piece_index]
        new_position = (current_position + spaces) % 52
        if self.board[new_position] != 0:
            opponent = self.get_opponent_at_position(new_position)
            if opponent:
                opponent_piece_index = self.get_opponent_piece_index(opponent, new_position)
                self.piece_positions[opponent][opponent_piece_index] = 0
                print(f"{player} captured {opponent}'s piece at position {new_position}!")
        self.piece_positions[player][piece_index] = new_position
        self.board[new_position] = self.current_player_index + 1

    def is_piece_at_home(self, piece_index):
        player = self.players[self.current_player_index]
        return self.piece_positions[player][piece_index] == 0

    def is_piece_at_safe_house(self, piece_index):
        player = self.players[self.current_player_index]
        position = self.piece_positions[player][piece_index]
        return position in [10, 21, 32, 43]

    def get_opponent_at_position(self, position):
        for i, player in enumerate(self.players):
            if i != self.current_player_index:
                for j, piece_position in enumerate(self.piece_positions[player]):
                    if piece_position == position:
                        return player
        return None

    def get_opponent_piece_index(self, opponent, position):
        for i, piece_position in enumerate(self.piece_positions[opponent]):
            if piece_position == position:
                return i

    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f"\n{player}'s turn:")
        roll = self.roll_dice()
        print(f"{player} rolled a {roll}.")
        for i in range(4):
            if self.is_piece_at_home(i):
                print(f"Piece {i + 1} is at home. You can move it out with a roll of 6.")
            else:
                print(f"Piece {i + 1} is at position {self.piece_positions[player][i]}.")
        piece_index = int(input("Enter the piece number you'd like to move (1-4): ")) - 1
        if self.is_piece_at_home(piece_index) and roll != 6:
            print("You can only move a piece out of home with a roll of 6.")
        else:
            self.move_piece(piece_index, roll)
            print(f"{player} moved piece {piece_index + 1} to position {self.piece_positions[player][piece_index]}.")
            if self.is_piece_at_safe_house(piece_index):
                print(f"{player}'s piece {piece_index + 1} is now at a safe house!")
        self.current_player_index = (self.current_player_index + 1) % 4

    def play_game(self):
        while True:
            self.play_turn()
            for player in self.players:
                if all(position != 0 and position >= 50 for position in self.piece_positions[player]):
                    print(f"\n{player} wins!")
                    return


game = LudoGame()
game.play_game()