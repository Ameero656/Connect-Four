class Engine():
    def __init__(self, game, player, enemy):
        self.ROWS = game.ROWS
        self.COLS = game.COLS
        self.player = player
        self.enemy = enemy


    def place_token(self, token, pos, game_board):
        for r in range(self.ROWS):  # 0->7 iteration
            selected_row = self.ROWS - r - 1  #becomes 7->0 iteration (down to up on 2d array)
            if game_board[selected_row][pos] == 0:  #checks if pos is avalible in the lowest row possible
                game_board[selected_row][pos] = token
                return game_board
    
    def is_game_over(self, game_board):
        for r in range(len(game_board)):
            for c in range(len(game_board[r])):
                #check if horizontal in range
                won = True
                if c + 3 < self.COLS: #check if horizontal in range
                    if game_board[r][c] != 0:
                        for checked_tile in range(4):
                            tile_value = game_board[r][checked_tile + c] 
                            if tile_value != game_board[r][c]: #check if consistant in tiles
                                won = False
                                break
                        if won:
                            return True
                won = True
                if r + 3 < self.ROWS:
                    if game_board[r][c] != 0:
                        for checked_tile in range(4):
                            tile_value = game_board[checked_tile + r][c]
                            if tile_value != game_board[r][c]:
                                won = False
                                break
                        if won:
                            return True
                won = True
                if r + 3 < self.ROWS and c + 3 < self.COLS:
                    if game_board[r][c] != 0:
                        for checked_tile in range(4):
                            tile_value = game_board[checked_tile + r][checked_tile + c]
                            if tile_value != game_board[r][c]:
                                won = False
                                break
                        if won:
                            return True
        return False

    def score_game_board(self, game_board, turn):
        if turn == 2:
            multiplier = -1
        else:
            multiplier = 1
        if self.is_game_over(game_board):
            return 10 * multiplier
        return 0

    def get_possible_moves(self, game_board):
        possible_moves = []
        for i, c in enumerate(game_board[0]):
            if c == 0:
                possible_moves.append(i)
        return possible_moves

    def minimax(self, depth, game_board, is_robot_turn):
        game_over = self.is_game_over(game_board)
        if game_over or depth == 0:
            return None, self.score_game_board(game_board, is_robot_turn)

        possible_moves = self.get_possible_moves(game_board)
        if is_robot_turn:
            best_move = None
            evaluation = -999999
            for move in possible_moves:
                new_game_board = game_board
                new_game_board = self.place_token(self.player, move, new_game_board)
                _, new_evaluation = self.minimax(depth-1, new_game_board, False)
                if new_evaluation > evaluation:
                    best_move = move
                    evaluation = new_evaluation
            return best_move, evaluation
        else:
            best_move = None
            evaluation = 999999
            for move in possible_moves:
                new_game_board = game_board
                new_game_board = self.place_token(self.enemy, move, new_game_board)
                _, new_evaluation = self.minimax(depth-1, new_game_board, True)
                if new_evaluation < evaluation:
                    best_move = move
                    evaluation = new_evaluation
            return best_move, evaluation

                