class Game():

	def __init__(self, ROWS, COLS):
		self.turn = 0
		self.game_board = []
		self.ROWS = ROWS
		self.COLS = COLS
		self.set_board()

	def set_board(self):
		for r in range(self.ROWS):
			self.game_board.append([])
			for c in range(self.COLS):
				self.game_board[r].append(0)

	def place_token(self, player, pos):
		if self.turn != player:  #if not player's turn
			return False
		if pos < 0 or pos > self.COLS:  #if pos is outside range of game_board
			return False
		if self.game_board[0][pos] != 0:  #if no avalible space in pos
			return False

		for r in range(self.ROWS):  # 0->7 iteration
			selected_row = self.ROWS - r  #becomes 7->0 iteration (down to up on 2d array)
			if self.game_board[selected_row][pos] == 0:  #checks if pos is avalible in the lowest row possible
				self.game_board[selected_row][pos] = player
				self.turn = abs(1 - self.turn)
				return True
		return False  #should never happen

	def display_game_board(self):
		for r in self.game_board:
			for c in self.game_board[0]:
				print(f"{c}|", end="")
			print("\n")
