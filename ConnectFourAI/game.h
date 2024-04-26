#pragma once

#include "engine.h"

#include <iostream>
#include <map>
#include <string>

class Game {
public:
	Game(const int ROWS, const int COLS);

	bool placeToken(int token, int pos);

	void displayGameboard();

	int swapTurn();

	void playerTurn();

	void engineTurn(int depth);

	bool isGameOver();

	int getTurn();

private:

	int turn;
	std::vector<std::vector<int>> gameboard;
	const int ROWS;
	const int COLS;

	Engine engine;

	std::map<int, std::string> tokenToColor;
	std::string defaultColor;
};


