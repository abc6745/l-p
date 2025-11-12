#include <iostream>
using namespace std;
#define N 8

int board[N][N];

bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++)
        if (board[i][col])
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (int i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQ(int row) {
    if (row >= N)
        return true;

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;
            if (solveNQ(row + 1))
                return true;
            board[row][col] = 0;
        }
    }
    return false;
}

void printBoard() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << board[i][j] << " ";
        cout << endl;
    }
}

int main() {
    board[0][0] = 1;

    if (solveNQ(1))
        printBoard();
    else
        cout << "No solution exists\n";

    return 0;
}
