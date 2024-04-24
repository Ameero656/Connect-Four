from game import Game


def main():
	game_instance = Game(7, 8)
	game_instance.place_token(1, 3)
	game_instance.place_token(2, 3)
	game_instance.display_game_board()


if __name__ == "__main__":
	main()
