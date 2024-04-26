#include "game.h"

int main() {
	Game game(6, 7);

	bool gameOver = false;

	while (!gameOver) {
		game.playerTurn();
		game.engineTurn(6);
		if (game.isGameOver()) {
			std::cout << "Token " << game.getTurn() << " Wins!\n";
			break;
		}
	}
}