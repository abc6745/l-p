#include <iostream>
using namespace std;

int main() {
    int weight[] = {10, 40, 20, 30};
    int profit[] = {60, 40, 100, 120};
    int capacity = 50;
    int n = sizeof(profit) / sizeof(profit[0]);

    double ratio[n];
    for (int i = 0; i < n; i++) {
        ratio[i] = (double)profit[i] / weight[i];
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (ratio[i] < ratio[j]) {
                swap(ratio[i], ratio[j]);
                swap(profit[i], profit[j]);
                swap(weight[i], weight[j]);
            }
        }
    }

    double totalProfit = 0.0;
    int remaining = capacity;

    for (int i = 0; i < n; i++) {
        if (weight[i] <= remaining) {
            totalProfit += profit[i];
            remaining -= weight[i];
        } else {
            totalProfit += ratio[i] * remaining;
            break;
        }
    }

    cout << "Maximum Profit = " << totalProfit << endl;

    return 0;
}
