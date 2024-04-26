#include "game.h"

Game::Game(const int ROWS, const int COLS) : ROWS(ROWS), COLS(COLS), engine(2, 1) {
	turn = 1;
	
	gameboard = std::vector<std::vector<int>>(ROWS, std::vector<int>(COLS, 0));

	tokenToColor = {
		{0, "\033[0m"},
		{1, "\033[0;31m"},
		{2, "\033[0;34m"}
	};
	defaultColor = "\033[0m";
}

bool Game::placeToken(int token, int pos) {
	if (turn != token) return false;
	if (pos < 0 || pos > gameboard.size()) return false;
	if (gameboard[0][pos] != 0) return false;

	for (int r = gameboard.size(); r >= 0; r--) {
		if (gameboard[r][pos] == 0) {
			gameboard[r][pos] = token;
			swapTurn();
		}
	}
	return false; //Should never happen
}

void Game::displayGameboard() {
	for (int r = 0; r < gameboard.size(); r++) {
		std::cout << "|";
		for (int c = 0; c < gameboard[r].size(); c++) {
			std::string color = tokenToColor[gameboard[r][c]];
			std::cout << color << gameboard[r][c] << defaultColor << "|";
		}
		std::cout << "\n";
	}
}

int Game::swapTurn() {
	return turn == 1 ? 2 : 1;
}

void Game::playerTurn() {
	displayGameboard();
	int pos;
	bool placed = false;

	while (!placed) {
		std::cout << "Select Collumn to place Token:";
		pos = 3;
		placed = placeToken(turn, pos);
	}
	swapTurn();
}

void Game::engineTurn(int depth) {
	int pos;
	std::pair<int, int> evaluation = engine.eval(depth, gameboard, true);
	std::cout << "Best Move=" << evaluation.first << "|Eval=" << evaluation.second << "\n";
	placeToken(turn, evaluation.first);
}

bool Game::isGameOver() {
	return engine.isGameOver(gameboard);
}

int Game::getTurn() {
	return turn;
}
