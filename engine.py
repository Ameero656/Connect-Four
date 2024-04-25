class Engine():

    def __init__(self, game, player, enemy):
        self.ROWS = game.ROWS
        self.COLS = game.COLS
        self.player = player
        self.enemy = enemy

    def place_token(self, token, pos, game_board):
        for r in range(self.ROWS):  # 0->7 iteration
            selected_row = self.ROWS - r - 1  #becomes 7->0 iteration (down to up on 2d array)
            if game_board[selected_row][
                    pos] == 0:  #checks if pos is avalible in the lowest row possible
                game_board[selected_row][pos] = token
                return game_board

    def is_game_over(self, game_board):
        for r in range(len(game_board)):
            for c in range(len(game_board[r])):
                #check if horizontal in range
                won = True
                if c + 3 < self.COLS:  #check if horizontal in range
                    if game_board[r][c] != 0:
                        for checked_tile in range(4):
                            tile_value = game_board[r][checked_tile + c]
                            if tile_value != game_board[r][
                                    c]:  #check if consistant in tiles
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
                            tile_value = game_board[checked_tile +
                                                    r][checked_tile + c]
                            if tile_value != game_board[r][c]:
                                won = False
                                break
                        if won:
                            return True
                if r - 3 < self.ROWS and c + 3 < self.COLS:
                    if game_board[r][c] != 0:
                        for checked_tile in range(4):
                            tile_value = game_board[r - checked_tile][checked_tile + c]
                            if tile_value != game_board[r][c]:
                                won = False
                                break
                        if won:
                            return True
        return False

    def score_game_board(self, game_board, is_robot_turn):
        score = 0

        if is_robot_turn:
            multiplier = -1
            good_token = self.player
            bad_token = self.enemy
        else:
            multiplier = 1
            good_token = self.enemy
            bad_token = self.player

        if self.is_game_over(game_board):
            score += 10000 * multiplier

        for row in range(len(game_board)):
            for col in range(len(game_board[row])):
                
                if game_board[row][col] == good_token:
                    score+= 10 - abs(col - 3)
                elif game_board[row][col] == bad_token:
                    score+= 10 - abs(col - 3)
        
        return score

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
        best_move = None
        evaluation = -999999 if is_robot_turn else 999999
        for move in possible_moves:
            new_game_board = [row[:] for row in game_board]
            new_game_board = self.place_token(
                self.player if is_robot_turn else self.enemy, move,
                new_game_board)
            _, new_evaluation = self.minimax(depth - 1, new_game_board,
                                             not is_robot_turn)

            if is_robot_turn and new_evaluation > evaluation:
                best_move = move
                evaluation = new_evaluation
            elif not is_robot_turn and new_evaluation < evaluation:
                best_move = move
                evaluation = new_evaluation

        return best_move, evaluation
