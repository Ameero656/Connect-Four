from game import Game
from engine import Engine

def ai_vs_ai(depth1, depth2):
	
	game_instance = Game(6, 7)
	engine1 = Engine(game_instance, 1, 2)
	engine2 = Engine(game_instance, 2, 1)
	turn = 1
	
	game_instance.display_game_board()
	while True:
		if turn == 1:
			
			best_move, evaluation = engine1.minimax(depth1, game_instance.game_board, True)
			print(f"bM:{best_move}, eval:{evaluation}")
			game_instance.place_token(turn, best_move)
			turn = 2
			game_instance.display_game_board()
		else:
	
			best_move, evaluation = engine2.minimax(depth2, game_instance.game_board, True)
			print(f"bM:{best_move}, eval:{evaluation}")
			game_instance.place_token(turn, best_move)
			turn = 1
			game_instance.display_game_board()
		if engine1.is_game_over(game_instance.game_board):
			break
	

def player_vs_ai():

	game_instance = Game(6, 7)
	engine1 = Engine(game_instance, 1, 2)
	engine2 = Engine(game_instance, 2, 1)
	turn = 1

	game_instance.display_game_board()
	while True:
		print(f"Turn={turn}")
		if turn == 1:	
			valid = False
			while not valid:
				chosen_move = int(input("Move:"))
				valid = game_instance.place_token(turn, chosen_move)
			turn = 2
		else:

			best_move, evaluation = engine2.minimax(6,
			                                        game_instance.game_board,
			                                        True)
			print(f"bM:{best_move}, eval:{evaluation}")
			game_instance.place_token(turn, best_move)
			turn = 1
		game_instance.display_game_board()
		if engine1.is_game_over(game_instance.game_board):
			break


if __name__ == "__main__":
	player_vs_ai()
