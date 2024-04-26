#include "engine.h"

Engine::Engine(int maximizingToken, int minimizingToken) : maximizingToken(maximizingToken), minimizingToken(minimizingToken) {}

bool Engine::placeToken(int token, int pos, std::vector<std::vector<int>>& gameboard) { //returns if placed or not (if there is room)
	for (int r = gameboard.size(); r >= 0; r--) {
		if (gameboard[r][pos] == 0) {
			gameboard[r][pos] = token;
		}
	}
	return false;
}

bool Engine::isGameOver(std::vector<std::vector<int>> gameboard) {
	const int ROWS = gameboard.size();
	const int COLS = gameboard[0].size();
	bool isOver;

	for (int r = 0; r <ROWS; r++) {
		for (int c = 0; c < COLS; c++) {

			isOver = true; 
			if (c + 3 < COLS && gameboard[r][c] != 0) { //Horizontal
				for (int offset = 0; offset < 4; offset++) {
					if (gameboard[r][c + offset] != gameboard[r][c]) isOver = false;
				}
			}
			if (isOver) return true;

			isOver = true;
			if (r + 3 < ROWS && gameboard[r][c] != 0) { //Vertical
				for (int offset = 0; offset < 4; offset++) {
					if (gameboard[r + offset][c] != gameboard[r][c]) isOver = false;
				}
			}
			if (isOver) return true;

			isOver = true;
			if ((c + 3 < COLS && r + 3 < ROWS) && gameboard[r][c] != 0) { //Diagonal 1
				for (int offset = 0; offset < 4; offset++) {
					if (gameboard[r + offset][c + offset] != gameboard[r][c]) isOver = false;
				}
			}
			if (isOver) return true;

			isOver = true;
			if ((c + 3 < COLS && r - 3 >=0) && gameboard[r][c] != 0) { //Diagonal 2
				for (int offset = 0; offset < 4; offset++) {
					if (gameboard[r - offset][c + offset] != gameboard[r][c]) isOver = false;
				}
			}
			if (isOver) return true;

		}
	}
	return false;
}

int Engine::scoreGameboard(std::vector<std::vector<int>> gameboard, bool isMaximizingPlayer) {
	int score = 0;

	int mult = isMaximizingPlayer ? -1 : 1;
		
	if (isGameOver(gameboard)) score += 10000000 * mult;

	for (int r = 0; r < gameboard.size(); r++) {
		for (int c = 0; c < gameboard[0].size(); c++) {
			if (gameboard[r][c] == maximizingToken) score += (10 - abs(c - 3)) * mult;
			else if (gameboard[r][c] != 0) score -= (10 - abs(c - 3)) * mult;
		}
	}
	return score;
}

std::vector<int> Engine::getPossibleMoves(std::vector<std::vector<int>> gameboard) {
	std::vector<int> possibleMoves;

	for (int r = 0; r < gameboard.size(); r++) {
		if (gameboard[r][0] == 0) possibleMoves.push_back(r);
	}
	return possibleMoves;
}

void Engine::copyGameboard(std::vector<std::vector<int>>& oldGameboard, std::vector<std::vector<int>>& newGameboard) {
	for (int r = 0; r < oldGameboard.size(); r++) {
		for (int c = 0; c < oldGameboard[r].size(); c++) {
			newGameboard[r][c] = oldGameboard[r][c];
		}
	}
}

std::pair<int, int> Engine::eval(int depth, std::vector<std::vector<int>> gameboard, bool isMaximizingPlayer) {
	if (isGameOver(gameboard) || depth == 0) return {-1, scoreGameboard(gameboard, isMaximizingPlayer)};

	std::vector<int> possibleMoves = getPossibleMoves(gameboard);
	std::pair<int, int> evaluation = { -1, isMaximizingPlayer ? -999999 : 999999 };

	for (const auto& move : possibleMoves) {
		std::vector<std::vector<int>> newGameboard;
		copyGameboard(gameboard, newGameboard);

		bool placed = placeToken(isMaximizingPlayer ? maximizingToken : minimizingToken, move, newGameboard);
		if (!placed) return { -1, 0 };

		std::pair<int, int> newEvaluation = eval(depth - 1, newGameboard, !isMaximizingPlayer);

		if (isMaximizingPlayer && newEvaluation.second > evaluation.second) evaluation = newEvaluation;
		else if (!isMaximizingPlayer && newEvaluation.second < evaluation.second) evaluation = newEvaluation;
	}
	return evaluation;
}

