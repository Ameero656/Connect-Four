from game import Game
from engine import Engine


def main():
	
	game_instance = Game(7, 8)
	engine = Engine(game_instance, 2, 1)

	game_instance.place_token(1, 3)
	game_instance.place_token(2, 2)
	game_instance.place_token(1, 3)
	

	game_instance.display_game_board()

	best_move, evaluation = engine.minimax(5, game_instance.game_board, True)
	print(f"bM:{best_move}, eval:{evaluation}")

	

	


if __name__ == "__main__":
	main()
