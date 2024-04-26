#pragma once

#include <vector>

class Engine {
public:
	Engine(int maximizingToken, int minimizingToken);
	
	bool placeToken(int token, int pos, std::vector<std::vector<int>>& gameBoard);

	bool isGameOver(std::vector<std::vector<int>> gameBoard);

	int scoreGameboard(std::vector<std::vector<int>> gameBoard, bool isMaximizingPlayer);

	std::vector<int> getPossibleMoves(std::vector<std::vector<int>> game_board);

	std::pair<int, int> eval(int depth, std::vector<std::vector<int>> gameBoard, bool isMaximizingPlayer);

	void copyGameboard(std::vector<std::vector<int>>& oldGameboard, std::vector<std::vector<int>>& newGameboard);

private:
	int maximizingToken;
	int minimizingToken;
};
